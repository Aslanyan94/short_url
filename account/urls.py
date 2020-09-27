from django.urls import path
from .views import ShortUrlView, show_url, UrlDetailView, testing_js


urlpatterns = [
    path('', ShortUrlView.as_view(), name="home"),
    # path('', testing_js, name="home"),
    path('<slug:pk>/detail/', UrlDetailView.as_view(), name='url-detail'),
    path('<slug:id>/', show_url, name='show-url'),
]
