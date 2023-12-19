#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/2 12:25
# @Author : natsume
# @File : encrypt.py
# @Software: PyCharm
import hashlib
from django.conf import settings

def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()