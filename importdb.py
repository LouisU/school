# -*- coding: utf-8 -*-
import sys
import pymssql
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

msdb = pymssql.connect('10.66.223.205', 'mhmt', 'Meihao365.net', 'Qizhong')
ms_cursor = msdb.cursor()
sql = 'select Sys_UserInfoID, UserResnumber, UserCardNo, UserAccount, UserPwd, UserName, UserSex, InfoBeginTime, Age from sys_userinfo'
ms_cursor.execute(sql)
resultdata = ms_cursor.fetchall()



mydb = MySQLdb.connect('10.66.205.174', 'root', 'Meihao365@net', 'test')
my_cursor = mydb.cursor()
for row in resultdata:
   print row
   i=0
   for index in range(len(row)):
      if index == None:
         
   my_cursor.execute("INSERT into honghua_sys_userinfo(Sys_UserInfoID, UserResnumber, UserCardNo, UserAccount, UserPwd, UserName, UserSex, InfoBeginTime, stature, Age) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[7], row[8]))

my_cursor.close()
ms_cursor.close()












