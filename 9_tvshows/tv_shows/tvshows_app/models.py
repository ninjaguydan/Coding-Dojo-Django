from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        present = datetime.now()
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters long"
        
        #check for duplicates
        shows = Show.objects.all()
        for show in shows:
            if postData["title"] == show.title:
                errors['unique_title'] = f"{show.title} is already listed!"
        
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters long"

        #check if a date was entered
        if postData['rdate'] == True:
            #check if date is in the past
            if datetime.strptime(postData['rdate'], '%Y-%m-%d') > present:
                errors["release_date"] = f"{postData['rdate']} has not yet occured"
            
        if len(postData["desc"]) > 0 and len(postData["desc"]) < 10:
            errors["decsription"] = "Description should be at least 10 characters"
        return errors
        
class Show(models.Model):
    title = models.CharField(max_length = 99)
    network = models.CharField(max_length = 10)
    release_date = models.CharField(max_length = 50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()
