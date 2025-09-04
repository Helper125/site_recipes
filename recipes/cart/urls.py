from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:recipes_id>/', views.add_to_cart, name='cart_add'),
    path('cart/remove/<int:recipes_id>', views.remove_cart, name='cart_remove'),
    path('cart_en/', views.cart_detail_en, name='cart_detail_en'),
    path('cart_en/add/<int:recipes_id>', views.add_to_cart_en, name='cart_en_add'),
    path('cart_en/remove/<int:recipes_id>', views.remove_cart_en, name='cart_en_remove')
]