#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/1 16:25
# @Author : natsume
# @File : bootstrap.py
# @Software: PyCharm
from django import forms

class BootStrap:
    bootstrap_exclude_fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
                field.widget.attrs["rows"] = 1
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label,
                    "rows": 1
                }

class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass

class BootStrapForm(BootStrap, forms.Form):
    pass
