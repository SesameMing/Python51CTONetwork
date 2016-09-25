#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-25 11:51

from xml.etree import ElementTree as ET

root = ET.Element('famliy')

son1 = ET.Element("son", {"name": "son1"})
son2 = ET.Element("son", {"name": "son2"})

grandson1 = ET.Element("grandson", {"name": "grandson1"})
grandson2 = ET.Element("grandson", {"name": "grandson2"})

son1.append(grandson1)
son2.append(grandson2)

root.append(son1)
root.append(son2)

tree = ET.ElementTree(root)
tree.write("oooo.xml", encoding="utf-8", short_empty_elements=False)
