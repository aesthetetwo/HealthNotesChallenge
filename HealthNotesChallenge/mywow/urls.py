from django.urls import views
from django.urls.resolvers import URLPattern
from . import views


urlpaterns = [
    path('', views.mywow , name="mywow"),
]