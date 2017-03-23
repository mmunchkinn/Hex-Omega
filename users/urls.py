from django.conf.urls import url

from . import views
from .Claudia import views as cv
from .Xav import views as xv

urlpatterns = [
    # index page
    url(r'^$', views.index, name="index"),
    # login page
    url(r'^login/$', views.login_auth_2, name='login_page'),
    # log out view
    url(r'^logout/$', views.jump_ship, name='jump_ship'),
    # create project
    url(r'^leader_user/(?P<username>[A-Z0-9][0-9]{7})/create/$', views.create_project, name="create_project"),
    # user delete view
    url(r'^user/(?P<username>[A-Z0-9][0-9]{7})/delete/(?P<d>[A-Z0-9][0-9]{7})/$', views.delete_admin, name="delete_admin"),
    # list of users
    url(r'^user/(?P<username>[A-Z0-9][0-9]{7})/list$', views.list_users, name="list_users"),

    # Home pages (now dummy pages)
    # the following will show list of open projects for the admin
    url(r'^admin_user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="admin_home"),
    # show, create and edit tasks for specific project
    # url(r'^leader_user/(?P<username>[A-Z0-9][0-9]{7})/$', views.leader_home, name="leader_home"),
    # Show tasks assigned to specific user and able to upload deliverable.
    url(r'^member_user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="member_home"),
    # user dispatch
    url(r'^user/(?P<username>[A-Z0-9][0-9]{7})/$', views.logged_in, name="user_logged_in"),

    # ----- Claudia
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/add_admin/$", cv.create_admin_user, name='add_admin'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/details/$", cv.get_admin_detail, name='display_admin'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/update/$", cv.update_admin_detail, name='update_admin'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/admin_list/$", cv.get_list_of_admins, name='list_of_admins'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/leader_list/$", cv.get_list_of_leaders, name='list_of_leaders'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/member_list/$", cv.get_list_of_members, name='list_of_members'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/update_adm/(?P<a>[A-Z0-9][0-9]{7})/$", cv.update_an_admin, name='update_admin_user'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/update_mem/(?P<m>[A-Z0-9][0-9]{7})/$", cv.update_member, name='update_member'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/update_lead/(?P<l>[A-Z0-9][0-9]{7})/$", cv.update_leader, name='update_leader'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/delete/(?P<d>[A-Z0-9][0-9]{7})/$", cv.delete_user, name='delete_user'),
    url(r"^member_user/(?P<username>[A-Z0-9][0-9]{7})/details/$", cv.get_member_detail, name='display_member'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/project/$", cv.display_all_projects, name='all_project'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/open_project/$", cv.display_open_projects, name='open_project'),
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/(?P<p>[a-zA-Z0-9_]{1,10})/project_detail/$", cv.project_information, name='project_detail'),
    # ----- Xav
    # Creating a leader falls under the admin's role.
    url(r"^admin_user/(?P<username>[A-Z0-9][0-9]{7})/add_leader/$", xv.create_leader_user, name='add_leader'),
    url(r"^leader_user/(?P<username>[A-Z0-9][0-9]{7})/details/$", xv.display_leader_detail, name='display_leader'),
    url(r"^leader_user/(?P<username>[A-Z0-9][0-9]{7})/update/$", xv.update_leader_detail, name='update_leader'),
    # ----- Other
    url(r'^user/list/$', views.get_list_of_users, name='list_of_users'),
]
