#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 2.正则表达式函数.py
@time: 2017/8/30 上午11:19
@desc:
'''
import re



# 1.match
# match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
# map(patter, string, flag)    # pattern:正则模型   string:要匹配的字符串   falgs:匹配模式
# re.I(re.IGNORECASE):    忽略大小写（括号内是完整写法，下同）
# M(MULTILINE):  多行模式，改变'^'和'$'的行为
# S(DOTALL):     点任意匹配模式，改变'.'的行为   使 . 匹配包括换行在内的所有字符
# L(LOCALE):     使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# U(UNICODE):    使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# X(VERBOSE):    详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：

pattern = re.compile(r"\w")
match = pattern.match('abcdefab111111')
if match:
    print(match.group())     # 获取匹配到的所有结果
    print(match.groups())    # 获取模型中匹配到的分组结果
    print(match.groupdict()) # 获取模型中匹配到的分组结果


