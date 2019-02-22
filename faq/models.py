from django.db import models

# Create your models here.


class Topic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tittle = models.CharField(max_length=100, blank=False)
    text = models.TextField()
