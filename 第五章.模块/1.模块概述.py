#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.模块概述.py
@time: 2017/8/21 下午2:33
@desc:
'''

import sys
import os

from mylib import accout
from mylib import commons


# 1.模块分类
#   Python中模块分为三种：自定义模块，第三方模块，内置模块


# 2.模块概述
#   导入一个py文件，解释器解释该py文件
#   导入一个包，解释器解释该包下的__init__.py文件
#   导入模块时将以sys.path作为基准，sys.path第一个值为当前路劲，其中site-packages存放的是所有第三方模块
#   如果sys.path路径列表没有你想要的路径，可以通过sys.path.append('路径')添加
print(sys.path)
print(os.path.abspath(__file__))                #拿到当前文件的路径
print(os.path.dirname(os.path.abspath(__file__)))            #拿到当前文件上一级目录的路径
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))          #拿到当前文件上上级目录的路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))          #将当前文件上上级目录添加到sys.path中


# 3.导入模块的方式
#   import module
#   from module.xx.xx import xx
#   from module.xx.xx import xx as rename
#   from module.xx.xx import *
accout.login()



# 4.另一种导入模式
# 默认导入模式
import requests
# __import__导入方式
__import__('requests')
# 如果是多层情况下
moudle = __import__('modlelib.commons', fromlist=True)   #如果不加上fromlist=True,只会导入mylib目录
ret = moudle.f1()
print(ret)              #F1

















