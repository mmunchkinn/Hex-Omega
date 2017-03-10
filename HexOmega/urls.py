"""HexOmega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from users import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^username/add/$', views.CreateAdminView.as_view(), name='add_admin'),
    url(r'^username/update/(?P<pk>[0-9]+)/$', views.UpdateAdmin.as_view(), name='update_admin'),
    url(r'^username/detail/(?P<pk>[0-9]+)/', views.DisplayAdminView.as_view(), name='admin_detail'),
    url(r'^leader/add/$', views.add_member, name='add_member'),
    url(r'^leader/(?P<pk>\d+)/$', views.DisplayMemberDetail.as_view(), name='member_detail'),
]
