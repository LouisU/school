# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pymssql
from django.shortcuts import render
from . import models
# Create your views here.


def testmssql(request):

    # user = models.User.objects.filter(name='a')
    # print user[0].cardno
    # return True

    conn = pymssql.connect(u'111.231.235.153:1234', u'mhmt', u'Meihao365.net', u'Qizhong')
    cursor = conn.cursor()
    cursor.execute("select * from Sys_UserInfo where sys_userinfoid=7")
    list = cursor.fetchone()
    print list
    cursor.close()
    return list
