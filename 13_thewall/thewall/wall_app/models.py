from django.db import models
from login_app.models import *

class ContentManager(models.Manager):
    def validator(self, formData):
        errors = {}
        if len(formData) < 1:
            errors["message"] = "Please type something. Anything."
        return errors


# Create your models here.
class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name = "messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ContentManager()

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name = "comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name = "comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ContentManager()