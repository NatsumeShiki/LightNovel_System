#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 14:44
# @Author : natsume
# @File : author.py
# @Software: PyCharm
from django.shortcuts import render, redirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

class AuthorModelForm(BootStrapModelForm):
    class Meta:
        model = models.Author
        exclude = ['author_id']

def author_list(request):
    form = AuthorModelForm()
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.Author.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        'form': form,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data
    }
    return render(request, 'author_list.html', context)

# 添加作者
@csrf_exempt
def author_add(request):
    form = AuthorModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

# 删除作者
def author_delete(request):
    uid = request.GET.get("uid")
    exists = models.Author.objects.filter(author_id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "数据不存在"})
    models.Author.objects.filter(author_id=uid).delete()
    return JsonResponse({"status": True})

# 点击修改查询该作者的信息
def author_detail(request):
    uid = request.GET.get("uid")
    row_dict = models.Author.objects.filter(author_id=uid).values("name", "gender", "date", "email").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)

@csrf_exempt
def author_edit(request):
    uid = request.GET.get("uid")
    row_object = models.Author.objects.filter(author_id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在"})
    form = AuthorModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})