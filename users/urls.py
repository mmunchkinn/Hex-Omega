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

    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/add_admin/$", views.create_admin_user, name='add_admin'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/details/$", views.get_admin_detail, name='display_admin'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/update/$", views.update_admin_detail, name='update_admin'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/list/$", views.get_list_of_users, name='list_of_users'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/delete/(?P<d>[a-zA-Z0-9_]{7,10})/$", views.delete_user, name='delete_user'),
    url(r"^member_user/(?P<username>[a-zA-Z0-9_]{7,9})/details/$", views.get_member_detail, name='display_member'),
    url(r"^member_user/(?P<username>[a-zA-Z0-9_]{7,9})/update/$", views.edit_member_information, name='update_member'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/project/$", views.display_all_projects, name='all_project'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/open_project/$", views.display_open_projects, name='open_project'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/(?P<p>[a-zA-Z0-9_]{1,10})/project_detail/$", views.project_information, name='project_detail'),
]