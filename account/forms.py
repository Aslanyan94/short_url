from django import forms
from account.models import ShortUrl


class URLForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ('base_url',)
