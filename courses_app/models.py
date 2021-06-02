from django.contrib.messages.api import error
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        if len(post_data['name'])< 5:
            errors['name_input']= "Course name must be at least 5 characters."
        if len(post_data['des'])< 15:
            errors['des_input']= "Course description must be at least 15 characters."
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, post_data):
        errors= {}
        if len(post_data['comment'])< 5:
            errors['comment_input']= "Comment must be at least 10 characters."
        return errors

class Description(models.Model):
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Course(models.Model):
    cor_name= models.CharField(max_length=100)
    description= models.OneToOneField(Description, related_name="course", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects= CourseManager()

class Comment(models.Model):
    content= models.CharField(max_length=255)
    course= models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects= CommentManager()