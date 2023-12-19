#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 14:45
# @Author : natsume
# @File : lightnovel.py
# @Software: PyCharm
from django.shortcuts import render, redirect
from django import forms

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

class LightNovelModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['book_id', 'image']
    class Meta:
        model = models.LightNovel
        fields = "__all__"

def lightnovel_list(request):
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.LightNovel.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data
    }
    return render(request, 'lightnovel_list.html', context)

def lightnovel_add(request):
    title = "添加小说"
    if request.method == "GET":
        form = LightNovelModelForm()
        return render(request, 'lightnovel_add.html', {'form': form, 'title': title})
    form = LightNovelModelForm(data=request.POST, files=request.FILES)
    if(form.is_valid()):
        form.save()
        return redirect("/lightnovel/list/")
    return render(request, 'lightnovel_add.html', {'form': form, 'title': title})

def lightnovel_detail(request, nid):
    obj = models.LightNovel.objects.filter(book_id=nid).first()
    return render(request, 'lightnovel_detail.html', {'obj': obj})

def lightnovel_edit(request, nid):
    title = "修改小说"
    if request.method == "GET":
        row_object = models.LightNovel.objects.filter(book_id=nid).first()
        form = LightNovelModelForm(instance=row_object)
        return render(request, 'lightnovel_edit.html', {'form': form, 'title': title, 'img': row_object.image})
    row_object = models.LightNovel.objects.filter(book_id=nid).first()
    form = LightNovelModelForm(data=request.POST, files=request.FILES, instance=row_object)
    if(form.is_valid()):
        form.save()
        return redirect('/lightnovel/list/')
    return render(request, 'lightnovel_edit.html', {'form': form, 'title': title})

def lightnovel_delete(request, nid):
    models.LightNovel.objects.filter(book_id=nid).delete()
    return redirect('/lightnovel/list/')