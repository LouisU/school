# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Sys_UserInfo(models.Model):

    Sys_UserInfoID = models.IntegerField(primary_key=True) #int  IDENTITY(1,1) NOT NULL,
    UserResnumber = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT ('0') NULL,
    UserCardNo = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    UserAccount = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT ('0') NULL,
    UserPwd = models.TextField(max_length=400, null=True) #nvarchar(200) COLLATE Chinese_PRC_CI_AS DEFAULT ('0') #NULL,
    UserName = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT '' NULL,
    UserSex = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT ((0)) NULL,
    # Sys_CPhysicalID = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # CardType = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # Sys_CGroupID = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT ((3)) NULL,
    # CardID = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # Birthday = models.DateTimeField(null=True) #datetime  NULL,
    # Email = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # PhoneNum] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT '' NULL,
    # ImportenPostID] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # EntryTime] = models.DateTimeField(null=True) #ddatetime  NULL,
    # DeleteMark] = models.IntegerField(default=1, null=True) #int DEFAULT ((1)) NULL,
    # User_Remark] = models.TextField(max_length=100, null=True) #nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
    # PostLevel] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # IsSuperManager] = models.IntegerField(null=True) #int  NULL,
    # Sys_CorpID] = models.IntegerField(null=True) #int  NULL,
    # CorpInNO] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # LastLoginDate] = models.DateTimeField(null=True) #ddatetime  NULL,
    # QQNumber] = models.TextField(max_length=100, null=True) #nvarchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
    # WeiXin] = models.TextField(max_length=100, null=True) #nvarchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
    # Sys_OrganizationID] = models.IntegerField(null=True) #int  NULL,
    # OrganizationInCode] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    InfoBeginTime = models.DateTimeField(null=True) #ddatetime  NULL,
    # InfoEndTime] = models.DateTimeField(null=True) #ddatetime  NULL,
    # MaritalStatusID] = models.IntegerField(null=True, default=0) #int DEFAULT ((0)) NULL,
    # MaritalNo] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # NationID] = models.IntegerField(null=True, default=0) #int DEFAULT ((0)) NULL,
    # ReligionID] = models.IntegerField(null=True) #int  NULL,
    # UserTypeId] = models.IntegerField(null=True) #int  NULL,
    # PoliticsID] = models.IntegerField(null=True) #int  NULL,
    # WorkTypeID] = models.IntegerField(null=True) #int DEFAULT ((0)) NULL,
    # Stature = models.FloatField() #numeric(8,2)  NULL,
    # [Weight] numeric(8,2)  NULL,
    # IssuingAuthority] = models.TextField(max_length=800, null=True) #nvarchar(400) COLLATE Chinese_PRC_CI_AS  NULL,
    # NativeID = models.IntegerField(null=True, default=0) #int DEFAULT ((0)) NULL,
    # AccountTypeID = models.IntegerField(null=True) #int  NULL,
    # [CityName] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # [Postalcode] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # [Cellphone] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # [EmergencyContact] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # [EmergencyRelation] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # [EmergencyContactCellphone] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    # [LodgeBeginTime] = models.DateTimeField(null=True) #ddatetime  NULL,
    # [LodgeEndTime] = models.DateTimeField(null=True) #ddatetime  NULL,
    # [LodgeNo] = models.TextField(max_length=100, null=True) #nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
    # [AccountAddress] = models.TextField(max_length=800, null=True) #nvarchar(400) COLLATE Chinese_PRC_CI_AS  NULL,
    # [ComAddress] = models.TextField(max_length=800, null=True) #nvarchar(400) COLLATE Chinese_PRC_CI_AS  NULL,
    # [CreditCardNo] = models.TextField(max_length=100, null=True) #nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
    Age = models.IntegerField(null=True) #int  NULL,
    # [PostLevelID] = models.IntegerField(null=True, default=0) #int DEFAULT ((0)) NULL,


class User(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    cardno = ''

    def get_cardno(self):
        import pymssql
        msdb = pymssql.connect('10.66.223.205', 'mhmt', 'Meihao365.net', 'Qizhong')
        ms_cursor = msdb.cursor()
        sql = 'select UserCardNo from sys_userinfo where sys_userinfoid=%d' % self.pk
        ms_cursor.execute()
        row = ms_cursor.fetchone()
        self.cardno = row[0]

        return self.cardno



