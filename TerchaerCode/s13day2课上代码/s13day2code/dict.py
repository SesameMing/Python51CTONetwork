#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li


#name = [1,[121212,'ShanPao','DongBei'],4,[121212,'DaShanPao','DongBei']5,5,6,7]
#print(name.index(121212) )

id_db = {
    371471199306143632: {
        'name':"Alex LI",
        'age': 22,
        'addr': 'ShanDong'
    },
    22043549306143632: {
        'name':"ShanPao",
        'age': 24,
        'addr': 'DongBei'
    },
    220435493061436532: {
        'name':"DaShanPao",
        'age': 24,
        'addr': 'DongBei'
    },
}
#print(id_db)

#print(id_db[22043549306143632] )
#id_db[22043549306143632]['name'] = "WangMinghu"
#id_db[22043549306143632]['qq_of_wife'] = 38232354
#id_db[220435493061436532].pop("addr")
#v = id_db.get(22435493061436532)
#v = id_db[22435493061436532]
#print(v)


dic2 = {
    'name':'dssfdsfsf',
    220435493061436532: {
        'name':"WangWang",
    },
}
#id_db.update(dic2)


#print(id_db)
#print(id_db.items())
#print(id_db.values())
#print(id_db.keys())
#id_db.has_key(371471199306143632) #only in 2.x
371471199306143632 in id_db #  equals to above has_key(x)

#print(id_db.setdefault(37147119930614363223434,"hahha")) #取一个key,如果 不存在，就设置一个默认k,v值
#print(dict.fromkeys([1,2,34,4,5,6],'dddd') )
#print(id_db.popitem() )
#print(id_db)

#for k,v in id_db.items(): #效率低， 因为要有一个dict to list的转换过程
#    print(k,v)
product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi 2',19.9),
    ('Coffee',30),
    ('Tesla',820000),
    ('Bike',700),
    ('Cloth',200),
]

for key in id_db: #效率高
    print(key,id_db[key ])

