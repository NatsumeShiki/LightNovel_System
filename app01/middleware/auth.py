#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/3 10:44
# @Author : natsume
# @File : auth.py
# @Software: PyCharm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AutoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ['/login/', '/image/code/', '/regist/']:
            return

        info_dict = request.session.get('info')
        # print(info_dict)
        if info_dict:
            return

        return redirect('/login/')