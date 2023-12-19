"""LightNovelSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from app01.views import account, publisher, author, lightnovel, illustrator

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 登录
    path('', account.login),
    path('login/', account.login),
    path('regist/', account.regist),
    path('image/code/', account.image_code),
    path('logout/', account.logout),

    # 出版社
    path('publisher/list/', publisher.publisher_list),
    path('publisher/add/', publisher.publisher_add),
    path('publisher/<int:nid>/edit/', publisher.publisher_edit),
    path('publisher/delete/', publisher.publisher_delete),

    #作者
    path('author/list/', author.author_list),
    path('author/add/', author.author_add),
    path('author/delete/', author.author_delete),
    path('author/detail/', author.author_detail),
    path('author/edit/', author.author_edit),

    # 插画师
    path('illustrator/list/', illustrator.illustrator_list),
    path('illustrator/add/', illustrator.illustrator_add),
    path('illustrator/delete/', illustrator.illustrator_delete),
    path('illustrator/detail/', illustrator.illustrator_detail),
    path('illustrator/edit/', illustrator.illustrator_edit),

    # 轻小说
    path('lightnovel/list/', lightnovel.lightnovel_list),
    path('lightnovel/add/', lightnovel.lightnovel_add),
    path('lightnovel/<int:nid>/delete/', lightnovel.lightnovel_delete),
    path('lightnovel/<int:nid>/detail/', lightnovel.lightnovel_detail),
    path('lightnovel/<int:nid>/edit/', lightnovel.lightnovel_edit),
]
