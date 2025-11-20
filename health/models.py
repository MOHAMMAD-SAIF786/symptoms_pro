from django.db import models

# Create your models here.
class Contact(models.Model):
    title=models.CharField(max_length=100)
    team=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    office=models.CharField(max_length=200)
    working_hr=models.CharField(max_length=100)
    note=models.TextField()

    def __str__(self):
        return self.title
    

class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    message=models.TextField(null=True, blank=True,default="No note")

    def __str__(self):
        return self.name
    

class Feature(models.Model):
    title=models.CharField(max_length=100)
    feature_button=models.CharField(max_length=50)
    content=models.TextField(default="no content yet")

    def __str__(self):
        return self.title

class Working(models.Model):
    title=models.CharField(max_length=50)
    steps=models.CharField(max_length=200)
    step_discription=models.TextField()

    def __str__(self):
        return self.title 
    
class Discliamer(models.Model):
    important_disclaimer=models.TextField()
    footer=models.TextField()

    def __str__(self):
        return self.important_disclaimer