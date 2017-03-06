from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.default_login_page, name="default_login_page"),
    url(r'^login/([0,1])$', views.login_page, name="login_page"),
    url(r'^login_auth/$', views.login_auth, name="login_auth"),
]