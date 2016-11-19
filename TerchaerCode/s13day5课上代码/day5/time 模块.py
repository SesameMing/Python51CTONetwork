
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import  time
import datetime
#print(time.time())
#print(time.ctime())
#print(time.ctime(time.time()-86400))
time_obj = time.gmtime()
#print(time_obj)
#print("{year}-{month}".format(year=time_obj.tm_year,month=time_obj.tm_mon))
#print(time.localtime())
#tm = time.strftime("%H:%M:%S",time.localtime())
#tm = time.strptime("2016-05-6 15:06" , "%Y-%m-%d %H:%M")
#print(time.mktime(tm))
#print(datetime.date.today())
current_time = datetime.datetime.now() #
#print(current_time) #输出2016-01-26 19:04:30.335935
#print(current_time.timetuple()) #返回struct_time格式
#print(datetime.datetime.now() + datetime.timedelta(hours=10) )  #比现在加10天
time_obj = current_time.replace(2015,5)

print(current_time==time_obj)
print(type(time_obj))
#print(datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") )