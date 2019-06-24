#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   django_demo
# File          :   search2.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/24 19:26
# Software      :   PyCharm
# Description   :   简述
"""

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)