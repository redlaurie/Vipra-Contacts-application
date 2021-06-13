from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    Number = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-details', kwargs={'pk': self.pk})