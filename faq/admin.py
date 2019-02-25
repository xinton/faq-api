from django.contrib import admin
from .models import Topic, User, HelpfulTopic


# Register your models here.
admin.site.register(Topic)
admin.site.register(HelpfulTopic)
admin.site.register(User)