from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import CustomUser
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    priority = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)




