from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^0001/', views.index),
]
