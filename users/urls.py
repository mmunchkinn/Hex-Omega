from django.conf.urls import url

from . import views
from .Claudia import views as cv

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.login_auth_2, name='login_page'),
    url(r'^logout/$', views.jump_ship, name='jump_ship'),
    url(r'^user/(?P<username>[a-zA-Z0-9_]{7,9})/$', views.logged_in, name="user_logged_in"),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/add_admin/$", cv.create_admin_user, name='add_admin'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/details/$", cv.get_admin_detail, name='display_admin'),
    url(r"^admin_user/(?P<username>[a-zA-Z0-9_]{7,9})/update/$", cv.update_admin_detail, name='update_admin'),
]
