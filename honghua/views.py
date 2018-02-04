# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# import pymssql
from django.shortcuts import render
from .models import UserInfo as client
# Create your views here.


def testmssql(request):
    #
    # lou = louis.objects.create(city='nanchang', livein='shenzhen')
    # return True

    user = client.objects.get_queryset(name='a')
    print user[0].cardno
    return True

    # conn = pymssql.connect(u'111.231.235.153:1234', u'mhmt', u'Meihao365.net', u'Qizhong')
    # cursor = conn.cursor()
    # cursor.execute("select * from Sys_UserInfo where sys_userinfoid=7")
    # list = cursor.fetchone()
    # print list
    # cursor.close()
    # render(request, list)
