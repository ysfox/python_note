#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:"Qin Yong"


# 2.基本数据类型

# (1).数字
# int(整型),在32位机器上为32位,在64位机器上64位,另外需要注意在Python中定义在[-5,257]范围的整数是体检建立好放在小整数对象池中
# 不会被垃圾回收，因此所有位于这个范围内的整数使用的都是同一个对象，另外整数有很多方法，需要自己去查阅并实践


# (2).布尔值
# 真或假(1或0)


# (3).字符串
s = " hello world    "
# 字符串常用功能:移除空白、长度、索引、切片
# 移除空白
print(s.strip())
# 长度
print(len(s))
# 索引
print(s[5])
# 切片
print(s[2:4])

# (4).列表
list = ['sb', 'nb', '2b']
# 列表基本操作:索引、追加、删除、长度、切片、循环、包含
# 索引
print(list.index('nb'))
# 追加
list.append("ab")
print(list)
# 删除
del list[-1]
print(list)
# 长度
print(len(list))
# 切片
print(list[0:2])
# 循环
for item in list:
    print(item)
# 包含
if 'sb' in list:
    print("list contain sb")

# (5).元祖
tep = (11, 22, 33, 44, 55, 66)
# 元祖基本操作：索引、切片、循环、长度、包含
# 元祖和列表的区别：元祖里面的值不能修改


# (6).字典
dic = {"name": "sb", "age": 100}
# 字典基本操作：索引、新增、删除、键、值、键值对、循环、长度
# 索引
print(dic["name"])
# 新增
dic['sex'] = "man"
print(dic)
# 删除
del dic['sex']
print(dic)
# 键
print(dic.keys())
# 值
print(dic.values())
# 键值对
print(dic.items())
# 循环
for k in dic.keys():
    print(k)
for v in dic.values():
    print(v)
for k, v in dic.items():
    print(k + "-->", v)
# 长度
print(len(dic))



# (7)set集合，无序且不重复的元素集合
# 相关的函数请查阅定义