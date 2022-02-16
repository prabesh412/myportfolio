from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.exp , name="expense"),
    path('<int:id1>/', views.dele , name="delete"),
]
