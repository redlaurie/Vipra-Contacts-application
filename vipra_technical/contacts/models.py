from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    number = models.IntegerField(max_length=11,blank=True)

    def __str__(self):
        return self.name