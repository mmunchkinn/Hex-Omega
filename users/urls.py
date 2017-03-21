from django.conf.urls import url

from . import views
from .Claudia import views as cv
from .Xav import views as xv

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.login_auth_2, name='login_page'),
    url(r'^logout/$', views.jump_ship, name='jump_ship'),
    url(r'^user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="user_logged_in"),
    url(r'^user/(?P<username>[A-Z0-9][0-9]{7})/delete/(?P<d>[A-Z0-9][0-9]{7})/$', views.delete_admin, name="delete_admin"),
    url(r'^user/(?P<username>[A-Z0-9][0-9]{7})/list$', views.list_users, name="list_users"),
    # Home pages (now dummy pages)
    # the following will show list of open projects for the admin
    url(r'^admin_user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="admin_user_logged_in"),
    # show, create and edit tasks for specific project
    url(r'^leader_user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="leader_user_logged_in"),
    # Show tasks assigned to specific user and able to upload deliverable.
    url(r'^member_user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="member_user_logged_in"),
    # ----- Claudia
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/add_admin/$", cv.create_admin_user, name='add_admin'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/details/$", cv.get_admin_detail, name='display_admin'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/update/$", cv.update_admin_detail, name='update_admin'),
    # ----- Xav
    # Creating a leader falls under the admin's role.
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/add_leader/$", xv.create_leader_user, name='add_leader'),
    url(r"^leader_user/(?P<username>[A-Z0-9][0-9]{7})/details/$", xv.display_leader_detail, name='display_leader'),
    url(r"^leader_user/(?P<username>[A-Z0-9][0-9]{7})/update/$", xv.update_leader_detail, name='update_leader'),
]
