#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import copy
name = ['Alex',"jack",'Rain',[9,4,3,5] , 634,34,89,'Eric','Monica',9,'Fiona',3,65,3,2,6,8,2,4,7]
name3 = name.copy()
name4 = copy.deepcopy(name)

name[0] = "ALEX"
name[3][1] = 4444444444444444444444444
name3[3][2] ="HHHHHH"
print(name)
print(name3)
print("name4",len(name4) )

r = (1,2,3,4,5) #只读列表，元组





'''
#print(99 in name)
if 9 in name: #判断列表中是否存在一个元素
    num_of_ele = name.count(9)
    position_of_ele = name.index(9)
    #name[position_of_ele] = 999
    #print("[%s] 9 is/are in name , posistion:[%s]" % (num_of_ele, position_of_ele))
    print(name)

for i in range(name.count(9)):
    ele_index = name.index(9)
    name[ele_index] = 99999999999999

name.extend(name2) #扩展进来一个新的列表
#name.reverse()
#name2.sort()
print(name2)
#print(name2)

'''
