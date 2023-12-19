#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 13:14
# @Author : natsume
# @File : account.py
# @Software: PyCharm

from io import BytesIO

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.bootstrap import BootStrapForm, BootStrapModelForm
from app01.utils.code import check_code
from app01.utils.encrypt import md5

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        required=True
    )
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    print(request)
    if form.is_valid():
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        request.session["info"] = {'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/lightnovel/list/')
    return render(request, 'login.html', {'form': form})

class RegistForm(BootStrapModelForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        required=True
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
    class Meta:
        model = models.Admin
        fields = ["username", "password"]

def regist(request):
    if request.method == 'GET':
        form = RegistForm()
        return render(request, 'regist.html', {'form': form})
    form = RegistForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error('code', "验证码错误")
            return render(request, 'regist.html', {'form': form})

        # print(form.cleaned_data)
        form.save()
        return redirect('/login/')
    return render(request, 'regist.html', {'form': form})

def image_code(request):
    img, code_string = check_code()
    # print(code_string)

    # 写入到自己的session中
    request.session['image_code'] = code_string
    # 设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())

def logout(request):
    request.session.clear()
    return redirect('/login/')