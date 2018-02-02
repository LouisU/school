# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
# Create your views here.


def testmssql(request):

    user = models.User.objects.filter(name='a')
    print user[0].cardno
    return True

#     conn = pymssql.connect('10.66.223.205', 'mhmt', 'Meihao365.net', 'Qizhong')
#     cursor = conn.cursor()
#     cursor = cursor.execute("select username from Sys_UserInfo where sys_userinfoid=7")
#     list = cursor.fetchone()
#     cursor.close()
#     return list
