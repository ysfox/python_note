#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 4.内置模块os.py
@time: 2017/8/21 下午3:37
@desc:
'''

import os
# os.getcwd()获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())
# os.chdir("dirname")改变当前脚本工作目录；相当于shell下cd
print(os.chdir('/Users/apple/Desktop/'))
print(os.getcwd())
# os.curdir返回当前目录: ('.')
print(os.curdir)
# os.pardir获取当前目录的父目录字符串名：('..')
print(os.pardir)
# os.makedirs('dir1/dir2')可生成多层递归目录，存在则报错
os.makedirs('/Users/apple/Desktop/1/2/3')
# os.removedirs('dirname1')若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推，只删除空文件夹
os.removedirs('/Users/apple/Desktop/1/2/3')
# os.mkdir('dirname')生成单级目录；相当于shell中mkdir dirname
os.mkdir('/Users/apple/Desktop/111')
# os.rmdir('dirname')删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.rmdir('/Users/apple/Desktop/111')
# os.listdir('dirname')列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.listdir('/Users/apple/Desktop/'))
# os.remove()删除一个文件
os.remove('/Users/apple/Desktop/1.txt')
# os.rename("oldname","new")重命名文件/目录
os.rename('/Users/apple/Desktop/2.txt', '/Users/apple/Desktop/aaa.txt')
# os.stat('path/filename')获取文件/目录信息
print(os.stat('/Users/apple/Desktop/aaa.txt'))
# os.sep操作系统特定的路径分隔符，win下为"\\",Linux下为"/"

# os.linesep当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"

# os.pathsep用于分割文件路径的字符串

# os.name字符串指示当前使用平台。win->'nt'; Linux->'posix'

# os.system("bash command")运行shell命令，直接显示

# os.environ获取系统环境变量

# os.path.abspath(path)返回path规范化的绝对路径

# os.path.split(path)将path分割成目录和文件名二元组返回

# os.path.dirname(path)返回path的目录。其实就是os.path.split(path)的第一个元素

# os.path.basename(path)返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

# os.path.exists(path)如果path存在，返回True；如果path不存在，返回False

# os.path.isabs(path)如果path是绝对路径，返回True

# os.path.isfile(path)如果path是一个存在的文件，返回True。否则返回False

# os.path.isdir(path)如果path是一个存在的目录，则返回True。否则返回False

# os.path.join(path1[, path2[, ...]])将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

# os.path.getatime(path)返回path所指向的文件或者目录的最后存取时间

# os.path.getmtime(path)返回path所指向的文件或者目录的最后修改时间
