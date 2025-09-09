from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (index_ua, registerUser, login, logout, recipes_more, translation_bd, index_en, recipes_more_en, delete_comment, delete_comment_en,
                    user_profil, update_recipes)

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
    path('myprofil/51a673d40841d13q9s33a4825s5139b3348f255516g734084ds126d055502d7223024d97481f6935d6871sd44375570g0260ss6d055502d<int:id_user>6d055502d7223024d97481f6935d6871sd44375570g0260ss/', user_profil, name='myprofil'),
    path('update_recipes/<int:id_recipes>/', update_recipes, name='update_recipes')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)