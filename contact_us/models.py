from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    number = models.IntegerField(max_length=13)
    message=models.TextField()
