#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 6.内置模块hashlib.py
@time: 2017/8/22 下午3:58
@desc:
'''

import hashlib

# 1.hashlib用于加密先关操作，代替了md5模块和sha模块，主要提供了SHA1,SHA224,SHA256,SHA384,SHAR512和MD5算法
######## md5 #########
# (方法一) update() 接收二进制类型
hash = hashlib.md5()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
# (方法二) 直接转换成二进制形式
print(hashlib.md5(b"admin").hexdigest())


######## sha1 ########
hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())


######## sha256 #######
hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())


######## sha384 ########
hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())


# ######## sha512 ########
hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())




# 2.加密虽然厉害，但是任然可以通过撞车来查找，所以需要自定义加盐key
hash = hashlib.md5(bytes('898oaFs09f', encoding="utf-8"))
hash.update(bytes('admin', encoding="utf-8"))
print(hash.hexdigest())
