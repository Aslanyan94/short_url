import json
import random

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

from account.models import ShortUrl
from account.forms import URLForm
from .random_string import random_string


@method_decorator(csrf_exempt, name='dispatch')
class ShortUrlView(CreateView):
    model = ShortUrl
    form_class = URLForm
    template_name = 'index.html'

    def form_valid(self, form):
        base_url = form.cleaned_data['base_url']
        try:
            short_url = ShortUrl.objects.get(base_url=base_url)
            short_url.count += 1
            short_url.save()
            id = short_url.id
        except ShortUrl.DoesNotExist:
            user_count = User.objects.count()
            form.instance.user = User.objects.get(pk=random.randint(1, user_count - 1))
            form.instance.short_url = f"{base_url}{random_string()}/"
            form.instance.count = 1
            form.save()
            id = form.instance.id
        return redirect("show-url", id=id)


class UrlDetailView(DetailView):
    model = ShortUrl
    template_name = "details.html"
    context_object_name = "detail_url"
    fields = ["user__username", "user__first_name", "user__email", "short_url", "base_url", "count"]


def show_url(request, id=None):
    data = ShortUrl.objects.get(id=id)
    return render(request, "url.html", context={'data': data})


@csrf_exempt
def testing_js(request):
    if request.method == "POST":
        data = json.dumps({"id": 1})
        return HttpResponse(content=data)
    return render(request, "index.html")
