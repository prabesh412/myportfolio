from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('post', views.post, name="post")
]
