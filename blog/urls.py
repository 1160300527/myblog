from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edt/(?P<article_id>[0-9]+)/$', views.article_change, name='edt'),
    url(r'^edt/action/$', views.edt_action, name='edt_action'),
    url(r'^delete/(?P<article_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^log/$', views.log, name="log"),
    url(r'^log/action/$', views.log_action, name="log_action"),
    url(r'^log/login/$', views.login, name="log_in"),
    url(r'^log/signup/$', views.signup, name="signup"),
]