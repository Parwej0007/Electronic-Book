"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from BookApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/create_book/', views.create_book, name='create_book'),
    url(r'^(?P<pk>\d+)/home/topic/$', views.Topic_view, name='topic'),
    url(r'^(?P<pk>\d+)/home/post/$', views.post_view, name='post'),
    # create form page and display when call
    url(r'^(?P<pk>\d+)/home/topic/create/$', views.create_topic, name='create_topic'),
    url(r'^(?P<pk>\d+)/home/post/create/$', views.create_post, name='create_post'),
    # when submit form insert/Update/delete data in database in TOPIC
    url(r'^(?P<pk>\d+)/home/topic/insert/$', views.insert_topic, name='insert_topic'),
    url(r'^(?P<pk>\d+)/home/topic/delete/$', views.delete_topic, name='delete_topic'),
    url(r'^(?P<pk>\d+)/home/topic/update/$', views.update_topic, name='update_topic'),
    # when submit form insert/Update/delete data in database in POST
    url(r'^(?P<pk>\d+)/home/post/insert/$', views.insert_post, name='insert_post'),
    url(r'^(?P<pk>\d+)/home/post/delete/$', views.delete_post, name='delete_post'),
    url(r'^(?P<pk>\d+)/home/post/update/$', views.update_post, name='update_post'),
    # for searching
    path('home/search/', views.search, name='search'),
    url(r'^(?P<pk>\d+)/search/delete/$', views.delete_book, name='delete_book'),
    path('about/', views.about, name='about'),


]
