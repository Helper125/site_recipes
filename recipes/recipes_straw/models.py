from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    STATUSE = [
        ('default', 'Default User'),
        ('editior', 'Editior User'),
        ('admin', 'Admin User'),
        ('moderator', 'Moderator User'),
        ('banned', 'Banned User')
    ]
    
    code_user = models.CharField(max_length=6, unique=True, blank=True)
    username = models.CharField(max_length=150, unique=False, blank=True, null=False)
    email = models.EmailField(unique=True, validators=[validate_email], blank=True)
    status = models.CharField(max_length=100, choices=STATUSE, default='default_user')
    photos_profil = models.ImageField(upload_to='img_profil/', default='img_profil/default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.code_user:
            self.code_user = str(uuid.uuid4())[:6].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"

class Recipes_UA_EN(models.Model):
    name_ua = models.CharField(max_length=100, blank=False)
    description_ua = models.TextField(blank=False)
    instruction_ua = models.TextField(blank=False)
    name_en = models.CharField(max_length=100)
    description_en = models.TextField()
    instruction_en = models.TextField()
    img = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.id, self.name_ua}___{self.name_en}"

class CommentUsers(models.Model):
    recipe = models.ForeignKey(Recipes_UA_EN, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment, "---", self.user}"