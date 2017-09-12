#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF


import configparser

# 1、获取所有节点
config = configparser.ConfigParser()
config.read('configfile', encoding='utf-8')
ret = config.sections()
print(ret)

# 2、获取指定节点下所有的键值对
config = configparser.ConfigParser()
config.read('configfile', encoding='utf-8')
ret = config.items('bitbucket.org')
print(ret)

# 3、获取指定节点下所有的建
config = configparser.ConfigParser()
config.read('configfile', encoding='utf-8')
ret = config.options('bitbucket.org')
print(ret)

# 4、获取指定节点下指定key的值
config = configparser.ConfigParser()
config.read('configfile', encoding='utf-8')
v = config.get('bitbucket.org', 'compression')
# v = config.getint('section1', 'k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')
print(v)


# 5、检查、删除、添加节点
config = configparser.ConfigParser()
config.read('configfile', encoding='utf-8')
# 检查
has_sec = config.has_section('bitbucket.org')
print(has_sec)

# 添加节点
config.add_section("SEC_1")
config.write(open('configfile', 'w'))

# 删除节点
config.remove_section("SEC_1")
config.write(open('configfile', 'w'))


# 6、检查、删除、设置指定组内的键值对
config = configparser.ConfigParser()
config.read('configfile', encoding='utf-8')
# 检查
has_opt = config.has_option('bitbucket.org', 'serveraliveinterval')
print(has_opt)
# 删除
config.remove_option('bitbucket.org', 'serveraliveinterval')
config.write(open('configfile', 'w'))
# 设置
config.set('bitbucket.org', 'compression', "no")
config.write(open('configfile', 'w'))

