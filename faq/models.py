from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Topic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()

    def __str__(self):
        return self.title

""" 
    Custom user model
"""
class User(AbstractUser):
    def __str__(self):
        return self.username


class HelpfulTopic(models.Model):
    user = models.ForeignKey("User", null=False, on_delete=models.PROTECT)
    topic = models.ForeignKey("Topic", null=False, on_delete=models.PROTECT)
    helpful= models.BooleanField(default=False)