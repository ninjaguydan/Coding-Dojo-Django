from django.db import models
from login_app.models import *

class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title is required"
        if len(postData['desc']) < 5:
            errors["Description"] = "Description must be at least 5 characters"
        return errors


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded", on_delete = models.CASCADE)
    users = models.ManyToManyField(User, related_name = "books")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = BookManager()