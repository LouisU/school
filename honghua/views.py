# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
# Create your views here.


def testmssql(request):
    adduser = models.User.objects.create(name='a')
    user = models.User.objects.filter(name='a')
    userinfoid = user[0].pk
    return

#     conn = pymssql.connect('10.66.223.205', 'mhmt', 'Meihao365.net', 'Qizhong')
#     cursor = conn.cursor()
#     cursor = cursor.execute("select username from Sys_UserInfo where sys_userinfoid=7")
#     list = cursor.fetchone()
#     cursor.close()
#     return list
