from django.contrib import admin

from .models import Recipes_UA_EN, CommentUsers

# Register your models here.
@admin.register(Recipes_UA_EN)
class RecipesAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentUsers)
class CommentsUsers(admin.ModelAdmin):
    list_filter = ('user', 'created_at')