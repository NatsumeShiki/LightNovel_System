#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 14:45
# @Author : natsume
# @File : illustrator.py
# @Software: PyCharm
from django.shortcuts import render, redirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

class IllustratorModelForm(BootStrapModelForm):
    class Meta:
        model = models.Illustrator
        exclude = ['illustrator_id']

# 插画师列表
def illustrator_list(request):
    form = IllustratorModelForm()
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.Illustrator.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        'form': form,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data
    }
    return render(request, 'illustrator_list.html', context)

# 添加插画师
@csrf_exempt
def illustrator_add(request):
    form = IllustratorModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

# 删除插画师
def illustrator_delete(request):
    uid = request.GET.get("uid")
    exists = models.Illustrator.objects.filter(illustrator_id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "数据不存在"})
    models.Illustrator.objects.filter(illustrator_id=uid).delete()
    return JsonResponse({"status": True})

# 点击修改查询该插画师的信息
def illustrator_detail(request):
    uid = request.GET.get("uid")
    row_dict = models.Illustrator.objects.filter(illustrator_id=uid).values("name", "gender", "date", "email").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)

@csrf_exempt
def illustrator_edit(request):
    uid = request.GET.get("uid")
    row_object = models.Illustrator.objects.filter(illustrator_id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在"})
    form = IllustratorModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})