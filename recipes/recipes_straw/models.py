from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipes_UA_EN(models.Model):
    name_ua = models.CharField(max_length=100, blank=False)
    description_ua = models.TextField(blank=False)
    instruction_ua = models.TextField(blank=False)
    name_en = models.CharField(max_length=100)
    description_en = models.TextField()
    instruction_en = models.TextField()
    img = models.CharField()

    def __str__(self):
        return f"{self.id, self.name_ua}___{self.name_en}"

class CommentUsers(models.Model):
    recipe = models.ForeignKey(Recipes_UA_EN, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment, "---", self.user}"