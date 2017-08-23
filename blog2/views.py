from django.shortcuts import render
from . import models
from django.http import HttpResponse
# Create your views here.


def index(request):
    first=models.myArtical.objects.get(pk=1)
    return render(request, 'blog2/index.html', {'first': first})