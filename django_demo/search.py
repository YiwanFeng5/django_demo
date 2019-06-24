#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   django_demo
# File          :   search.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/24 18:01
# Software      :   PyCharm
# Description   :   简述
"""

from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        msg = '您搜索的内容未：' + request.GET['q']
    else:
        msg = '你提交了空表单'

    return HttpResponse(msg)