from django.contrib import admin

from .models import Recipes_UA_EN, CommentUsers, CustomUser

# Register your models here.
@admin.register(CustomUser)
class Customusers(admin.ModelAdmin):
    list_filter = ('username', 'email', 'status', 'code_user')
    search_fields = ('username', 'email', 'status', 'code_user')
    list_display = ('username', 'code_user', 'email', 'status')

@admin.register(Recipes_UA_EN)
class RecipesAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentUsers)
class CommentsUsers(admin.ModelAdmin):
    list_filter = ('user', 'created_at')