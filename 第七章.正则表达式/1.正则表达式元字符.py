#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.正则表达式概述.py
@time: 2017/8/22 上午10:48
@desc:
'''

import re
# 1.元字符:　　. ^ $ * + ? { [ ] \ | ( )
# (1). .匹配一个除了换行符外所有字符 (通配符)
print(re.findall(r"b.d", 'Abcdefghijklmnopq'))          #['bcd']

# (2). ^　以....开头
print(re.findall(r"^Abcd", 'Abcdefghijklmnopq'))        #['Abcd']

# (3). $　以....结尾
print(re.findall(r"nopq$", 'Abcdefghijklmnopq'))        #['nopq']

# (4). *　匹配前导字符0到多次,相当于{0, }
print(re.findall(r"A.*e", 'Abcdefghijklmnopq'))         #['Abcde']

# (5). +　匹配前导字符1到多次,相当于{1, }
print(re.findall(r"ab1+", 'abcdefab111111'))            #['ab111111']

# (6). ?　匹配前导字符0到1次,相当于{0,1}
print(re.findall(r"ab1?", 'abcdefab111111'))            #['ab', 'ab1']

# (7). * + ? 都是按照贪婪模式进行匹配,如果要非贪婪模式需要在后面加个?
print(re.findall(r"ab1?", 'ab1cab1111dabfab111111'))    #['ab1', 'ab1', 'ab', 'ab1']    贪婪匹配
print(re.search(r"a(\d+?)", "a2345").group())           #a2
print(re.search(r"a(\d*?)", "a2345").group())           #a
print(re.search(r"a(\d*?)b", "a2345b").group())         #a234b   如果前后均有限定条件 ?不起作用

# (8).  ( ) 分组
print(re.search(r"(ab1)", "abcdefab111111").group())    #ab1

# (9).  { } 重复次数自定义
print(re.findall(r"ab1{3,9}", "abcdefab111111"))        #['ab111111']

# (10). [ ]　或,除了- \ ^ 3个元字符外,匹配[]中任意一个字符
print(re.findall(r"a[bc]d", "wwwwwabdxxxxx"))           #['abd']
print(re.findall(r"a[bc]d", "wwwwwacdxxxxx"))           #['acd']

# (11). \ 作用:
# \d  匹配任何十进制数, 相当于[0-9]
print(re.findall(r"\d", "wwwww1234xxxxx"))              #['1', '2', '3', '4']
# \D  匹配任何非数字字符 相当于[^0-9]
print(re.findall(r"\D", "wwwww1234xxxxx"))              #['w', 'w', 'w', 'w', 'w', 'x', 'x', 'x', 'x', 'x']
# \s  匹配任何空白字符 [ \t\n\r\f\v ]
print(re.findall(r"\s", "asdasd   "))                   #[' ', ' ', ' ']
# \S  匹配任何非空白字符 [^ \t\n\r\f\v ]
print(re.findall(r"\S", "asdasd   "))                   #['a', 's', 'd', 'a', 's', 'd']
# \w  匹配任何字母数字字符 [a-zA-Z0-9_]
print(re.findall(r"\w", "abc123^&*lm-\_"))              #['a', 'b', 'c', '1', '2', '3', 'l', 'm', '_']
# \W  匹配任何非字母数字字符 [^a-zA-Z0-9]
print(re.findall(r"\W", "abc123^&*lm-\_"))              #['^', '&', '*', '-', '\\']
# \b  匹配一个单词边界,单词和空格间的位置,匹配特殊字符(不单止空格)
print(re.findall(r"like\b", "I like Sooooo"))           #['like']
print(re.findall(r"abc\b","asdasd abc*"))               #['abc']
print(re.findall(r"abc\b","asdasd abc "))               #['abc']