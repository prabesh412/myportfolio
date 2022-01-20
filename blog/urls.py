from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.blog , name="blog"),
    path('upload/', views.upload , name='upload'),
    path('<int:blog_id>/', views.detail, name="detail"),
]
