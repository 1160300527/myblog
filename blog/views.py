from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def artitle_change(request):
    return render(request, 'blog/add_page.html')


def edt_action(request):
    title = request.POST['title']
    content = request.POST['content']
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})