from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from . import models
import datetime

# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def article_change(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/add_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/add_page.html', {'article': article})


def edt_action(request):
    alert = "yes"
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    time = request.POST.get('time', 'TIME')
    article_id = request.POST.get('article_id', '0')
    try:
        article = models.Article.objects.get(title=title)
        exist = True
    except:
        exist = False
    if not exist or (article_id != 0 and str(article.id) == str(article_id)):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if str(article_id) == '0':
            models.Article.objects.create(title=title, content=content, time=time)
            return render(request, 'blog/add_page.html', {'Alert': alert})
        else:
            article = models.Article.objects.get(pk=article_id)
            article.title = title
            article.content = content
            article.time = time
            article.save()
            return render(request, 'blog/add_page.html', {'Alert': alert, 'article': article})
    else:
        alert = "warning"
        if str(article_id) == '0':
            return render(request, 'blog/add_page.html', {'Alert': alert})
        else:
            return render(request, 'blog/add_page.html',
                          {'Alert': alert, 'article': models.Article.objects.get(pk=article_id)})


def delete(request, article_id):
    models.Article.objects.filter(pk=article_id).delete()
    return redirect('/index/')


def log(request):
    return render(request, 'blog/log.html')


def log_action(request):
    return render(request, 'blog/log.html', {'submit': "submit"})


def login(request):
    name = request.POST.get('name', None)
    password = request.POST.get('password', None)
    user = models.User.objects.filter(name=name)
    if check_password(password, user[0].password):
        return render(request, 'blog/alert.html', {'alert': "signup_successful"})
    else:
        return render(request, 'blog/alert.html',{'alert': "signup_failing"})


def signup(request):
    name = request.POST.get('name', None)
    password = make_password(request.POST.get('password', None), None, 'pbkdf2_sha256')
    email = request.POST.get('email', None)
    phone = request.POST.get('phone', None)
    models.User.objects.create(name=name, password=password, email=email, phone=phone)
    return render(request, 'blog/alert.html', {'alert': "signup_successful"})