"""optimus_logistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    url(r'^main/', main_views.index, name='index'),
    url(r'^reports/', main_views.reports, name='reports'),
    url(r'^newweek/', main_views.newweek, name='newweek'),
    url(r'^day/', main_views.day, name='day'),
    url(r'^addday/', main_views.addday, name='addday'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home, name='home')
]
