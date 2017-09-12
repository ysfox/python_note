#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 7.类的成员概述.py
@time: 2017/8/23 上午11:48
@desc:
'''

# 1.类的成员
# 类的成员分类如下:
# 字段,字段分为普通字段和静态字段
# 方法，方法分为普通方法，类方法和静态方法
# 属性，属性只有普通属性
# 注：所有成员中，只有普通字段的内容保存对象中，即：根据此类创建了多少对象，在内存中就有多少个普通字段。
# 而其他的成员，则都是保存在类中，即：无论对象的多少，在内存中只创建一份。