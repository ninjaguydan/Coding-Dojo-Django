from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['description'] = "Description should be at least 15 characters"
        
        courses = Course.objects.all()
        for course in courses:
            if postData['name'] == course.name:
                errors['unique_name'] = f"{course.name} is already listed"
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors["comment"] = "Please enter a comment"
        return errors

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()
