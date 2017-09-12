#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 7.外置模块requests.py
@time: 2017/8/22 下午4:24
@desc:
'''

import requests
import json
import urllib
from xml.etree import ElementTree as ET

# 1.requests GET请求无参数实例
response = requests.get('http://www.baidu.com')
response.encoding = 'utf-8'
result = response.text
print(result)

# 2.requests GET请求有参数实例
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('http://www.baidu.com', params=params)
result = response.text
print(result)

# 3.requests POST带参数的
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('http://www.baidu.com', data=params)
print(response.text)

# 4.requests POST请求头和数据实体
params = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
ret = requests.post('http://www.baidu.com', data=json.dumps(params), headers=headers)
print(ret.text)
print(ret.cookies)

# 5.python内置网络请求模块urllib
f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
result = f.read().decode('utf-8')
node = ET.XML(result)
print(node)
if node.text == 'Y':
    print("在线")
else:
    print("离线")
