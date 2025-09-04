from django.contrib import admin
from django.urls import path

from .views import (index_ua, registerUser, login, logout, recipes_more, translation_bd, index_en, recipes_more_en, delete_comment, delete_comment_en)

urlpatterns = [
    path('', index_ua, name="index_ua"),
    path('register/', registerUser, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('recips_more<int:id>/', recipes_more, name="recipes_more"),
    path('add_recipes', translation_bd, name="add_recipes"),
    path("en", index_en, name="index_en"),
    path("recipes_more_en<int:id>/", recipes_more_en, name="recipes_more_en"),
    path("delete_comment<int:id_comment>/", delete_comment, name="delete_comment"),
    path('delete_comment_en<int:id_comment>/', delete_comment_en, name='delete_comment_en'),
]