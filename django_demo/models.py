#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   django_demo
# File          :   models.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/24 17:28
# Software      :   PyCharm
# Description   :   简述
"""

from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)