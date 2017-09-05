from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from . import models
import datetime
from django.http import HttpResponse
import re


# Create your views here.


def index(request):
    request.session.set_expiry(0)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    request.session.set_expiry(0)
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def article_change(request, article_id):
    request.session.set_expiry(0)
    if str(article_id) == '0':
        return render(request, 'blog/add_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/add_page.html', {'article': article})


def edt_action(request):
    request.session.set_expiry(0)
    alert = "yes"
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    time = request.POST.get('time', 'TIME')
    article_id = request.POST.get('article_id', '0')
    patten = re.compile(r'\S')
    if not patten.match(title) or not patten.match(content):
        alert = "blank"
        if str(article_id) == '0':
            return render(request, 'blog/add_page.html', {'Alert': alert})
        else:
            return render(request, 'blog/add_page.html',
                          {'Alert': alert, 'article': models.Article.objects.get(pk=article_id)})
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
    request.session.set_expiry(0)
    models.Article.objects.filter(pk=article_id).delete()
    return redirect('/index/')


def log(request):
    request.session.set_expiry(0)
    return render(request, 'blog/log.html')


def login(request):
    request.session.set_expiry(0)
    name = request.POST.get('name',None)
    password = request.POST.get('password', None)
    user = models.User.objects.filter(name=name)
    if models.User.objects.filter(name=name):
        if check_password(password, user[0].password):
            request.session["log"] = "successful"
            request.session["user"] = name
            return HttpResponse("successful")
        else:
            request.session["log"] = "default"
            return HttpResponse("password_wrong")
    request.session["log"] = "default"
    return HttpResponse("name_none")


def signup(request):
    request.session.set_expiry(0)
    name = request.POST.get('name', None)
    password = make_password(request.POST.get('password', None), None, 'pbkdf2_sha256')
    email = request.POST.get('email', None)
    phone = request.POST.get('phone', None)
    if models.User.objects.filter(name=name):
        return HttpResponse("name_repeat")
    elif models.User.objects.filter(email=email):
        return HttpResponse("email_repeat")
    elif models.User.objects.filter(phone=phone):
        return HttpResponse("phone_repeat")
    else:
        models.User.objects.create(name=name, password=password, email=email, phone=phone)
        return HttpResponse("successful")


def session_get(request):
    value = request.session.get("log", default="default")
    if value == "default":
        return HttpResponse("default")
    else:
        return HttpResponse(request.session.get("user", default=None))


def out(request):
    if request.session.get("log",None):
        del request.session["log"]
        del request.session["user"]
        return HttpResponse("successful")
    else:
        return HttpResponse("default")


def search(request):
    title = request.POST.get("title", None)
    if models.Article.objects.filter(title=title):
        return HttpResponse(models.Article.objects.get(title=title).id)
    else:
        return HttpResponse("")