from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    time = models.CharField(max_length=32, default='0000-00-00 00:00:00')

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
