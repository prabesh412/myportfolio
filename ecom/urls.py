from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('api/', include('ecom.api.urls')),
    path('<int:product_id>/', views.detail, name="detail1"),
    path('cart/', views.cart1, name="cart1"),
]
