from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    time = models.CharField(max_length=32, default='0000-00-00 00:00:00')
    def __str__(self):
        return self.title