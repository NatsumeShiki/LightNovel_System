#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 13:50
# @Author : natsume
# @File : publisher.py
# @Software: PyCharm
from django.shortcuts import render, redirect
from django import forms

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

class PublisherModelForm(BootStrapModelForm):
    name = forms.CharField(
        label="出版社名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    date = forms.DateField(
        label="创立时间",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "dt"}),
        required=False
    )
    introduction = forms.CharField(
        label="简介",
        widget=forms.Textarea(attrs={"class": "form-control"}),
        required=False
    )

    class Meta:
        model = models.Publisher
        fields = ["name", "date", "introduction"]

# 列表
def publisher_list(request):
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.Publisher.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=8)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data
    }
    # print(queryset.values())
    return render(request, 'publisher_list.html', context)

# 添加
def publisher_add(request):
    if(request.method == "GET"):
        form = PublisherModelForm()
        return render(request, 'publisher_add.html', {'form': form})
    form = PublisherModelForm(data=request.POST)
    print(form)
    if (form.is_valid()):
        form.save()
        return redirect("/publisher/list")
    return render(request, 'publisher_add.html', {'form': form})

# 修改
def publisher_edit(request, nid):
    if(request.method == "GET"):
        row_object = models.Publisher.objects.filter(publisher_id=nid).first()
        form = PublisherModelForm(instance=row_object)
        return render(request, 'publisher_edit.html', {'form': form})
    row_object = models.Publisher.objects.filter(publisher_id=nid).first()
    form = PublisherModelForm(data=request.POST, instance=row_object)
    if(form.is_valid()):
        form.save()
        return redirect('/publisher/list/')
    return render(request, 'publisher_list.html', {'form': form})
# 删除
def publisher_delete(request):
    nid = request.GET.get("nid")
    models.Publisher.objects.filter(publisher_id=nid).delete()
    return redirect('/publisher/list/')