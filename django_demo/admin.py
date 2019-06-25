#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
# Project       :   django_demo
# File          :   admin.py
# Author        :   fengyiwan
# Email         :   ily19910525fyw@126.com
# Time          :   2019/6/25 13:20
# Software      :   PyCharm
# Description   :   简述
"""
from django.contrib import admin
from django_demo.models import Test, Contact, Tag


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name', )
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
