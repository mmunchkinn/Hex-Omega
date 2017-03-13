from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^login/$', views.default_login_page, name="default_login_page"),
    # url(r'^login/([0,1])$', views.login_page, name="login_page"),
    # url(r'^login_auth/$', views.login_auth, name="login_auth"),
    url(r'^login/$', views.login_auth_2, name='login_page'),
    url(r'^logout/$', views.jump_ship, name='jump_ship'),
    url(r'^user/(?P<username>[a-zA-Z0-9_]{7,9})/$', views.logged_in, name="user_logged_in"),

    url(r'^username/add/$', views.create_admin_user, name='add_admin'),
    url(r'^username/detail/(?P<pk>\d+)/', views.get_admin_detail, name='display_admin'),
    url(r'^username/update/(?P<pk>\d+)/', views.update_admin_detail, name='update_admin'),
]