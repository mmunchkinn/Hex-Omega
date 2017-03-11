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
    url(r'^user/(?P<username>[a-zA-Z0-9]{7,9})/$', views.logged_in, name="user_logged_in"),
    url(r'^username/add/$', views.CreateAdminView.as_view(), name='add_admin'),
    url(r'^username/update/(?P<pk>[0-9]+)/$', views.UpdateAdmin.as_view(), name='update_admin'),
    url(r'^username/detail/(?P<pk>[0-9]+)/', views.DisplayAdminView.as_view(), name='admin_detail'),
    url(r'^username/createLeader$', views.CreateLeaderView.as_view(), name='create_leader'),
    url(r'^username/leaderDetail/(?P<pk>[0-9]+)$', views.DisplayLeaderView.as_view(), name='leader_detail'),
    url(r'^leader/add/$', views.add_member, name='add_member'),
    url(r'^leader/(?P<pk>\d+)/$', views.DisplayMemberDetail.as_view(), name='member_detail'),
]