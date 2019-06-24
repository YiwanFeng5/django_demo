#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   django_demo
# File          :   testdb.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/24 17:41
# Software      :   PyCharm
# Description   :   简述
"""

from django.http import HttpResponse
from django_demo.models import Test


def testdb(request):
    """
    数据库操作
    :param request:
    :return:
    """
    test1 = Test.objects.get(id=1)
    test1.delete()
    return HttpResponse("<p>删除成功</p>")
