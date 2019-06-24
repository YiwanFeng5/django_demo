#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   django_demo
# File          :   view.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/24 17:04
# Software      :   PyCharm
# Description   :   简述
"""

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = "Hello, World ! "
    return render(request, 'hello.html', context)