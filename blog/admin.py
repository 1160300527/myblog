from django.contrib import admin
from .models import Article
from .models import User
# Register your models here.

admin.site.register(Article)
admin.site.register(User)