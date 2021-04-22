from django.db import models
import re
from datetime import timedelta, datetime

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors["first_name"] = "First Name must be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["last_name"] = "Last Name must be at least 2 characters"
        #check if date was entered
        if postData["bdate"] == "":
            errors["Date"] = "Please enter a date of birth"
        else:
            #check if date entered is from more than 13 years ago
            thirteen_years_ago = datetime.now() - timedelta(days = 365*13)
            if datetime.strptime(postData['bdate'], '%Y-%m-%d') > thirteen_years_ago:
                errors["Age"] = "Uh oh! Looks like you might be too young for an account"
        #check if email is valid
        if not email_regex.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
        #check if email is unique
        for user in User.objects.all():
            if postData["email"] == user.email:
                errors["email"] = "There is already an account using this email"
        
        if len(postData["pw"]) < 8:
            errors["password"] = "Password must be at least 8 characters"
        #check if pw and confirm pw fields match
        if postData["pw"] != postData["confirm-pw"]:
            errors["password"] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    bdate = models.DateTimeField(null = True)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()