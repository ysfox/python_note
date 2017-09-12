#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 8.内置模块xml.py
@time: 2017/8/22 下午4:59
@desc:
'''

from xml.etree import ElementTree as ET
from xml.dom import minidom


# 1.遍历XML文档的所有内容
############ 解析方式一 ############
# 打开文件，读取XML内容
str_xml = open('xo.xml', 'r').read()
# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)
# 顶层标签
print(root.tag)

############ 解析方式二 ############
# 直接解析xml文件
tree = ET.parse("xo.xml")
# 获取xml文件的根节点
root = tree.getroot()
# 顶层标签
print(root.tag)


# 2.遍历XML中指定的节点
# 遍历XML文档的第二层
for child in root:
    # 第二层节点的标签名称和标签属性
    print(child.tag, child.attrib)
    # 遍历XML文档的第三层
    for i in child:
        # 第二层节点的标签名称和内容
        print(i.tag, i.text)

# (2).遍历XML中所有的year节点
for node in root.iter('year'):
    # 节点的标签名称和内容
    print(node.tag, node.text)


# 3.修改节点内容
# 由于修改的节点时，均是在内存中进行，其不会影响文件中的内容，所以如果想要修改，则需要重新将内存中的内容写到文件
# 循环所有的year节点
for node in root.iter('year'):
    # 将year节点中的内容自增一
    new_year = int(node.text) + 1
    node.text = str(new_year)

    # 设置属性
    node.set('name', 'alex')
    node.set('age', '18')

    # 删除属性
    del node.attrib['name']

#保存文件
tree = ET.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')


# 4.创建XML文档
# 创建方式一
# 创建根节点
root = ET.Element("famliy")
# 创建节点大儿子
son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
# 创建小儿子
son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})
# 在大儿子中创建一个孙子
grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
grandson1.text = '孙子'
# 生成文档对象
et = ET.ElementTree(root)
# shorrt_empty_element = False    没有内容不自闭合
# xml_declaration = True          xml开头注释
et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)

# 创建方式二
# 创建根节点
root = ET.Element("famliy")
# 创建节点大儿子
son1 = ET.Element('son', {'name': '儿1'})
# 创建小儿子
son2 = ET.Element('son', {"name": '儿2'})
# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson2 = ET.Element('grandson', {'name': '儿12'})
son1.append(grandson1)
son1.append(grandson2)
# 把儿子添加到根节点中
root.append(son1)
root.append(son1)
# 生成文档对象
tree = ET.ElementTree(root)
tree.write('oooo.xml', encoding='utf-8', short_empty_elements=False)


# 创建方式三
# 创建根节点
root = ET.Element("famliy")
# 创建大儿子
# son1 = ET.Element('son', {'name': '儿1'})
son1 = root.makeelement('son', {'name': '儿1'})
# 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
son2 = root.makeelement('son', {"name": '儿2'})
# 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# grandson2 = ET.Element('grandson', {'name': '儿12'})
grandson2 = son1.makeelement('grandson', {'name': '儿12'})
# 把儿子添加到根节点中
son1.append(grandson1)
son1.append(grandson2)
# 把儿子添加到根节点中
root.append(son1)
root.append(son1)
# 生成文档对象
tree = ET.ElementTree(root)
tree.write('oooo.xml',encoding='utf-8', short_empty_elements=False)


# 创建方式四
# 由于原生保存的XML时默认无缩进，如果想要设置缩进的话， 需要修改保存方式：
def prettify(elem):
    """
    将节点转换成字符串，并添加缩进。
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def prettify(elem):
    """将节点转换成字符串，并添加缩进。
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

# 创建根节点
root = ET.Element("famliy")


# 创建大儿子
# son1 = ET.Element('son', {'name': '儿1'})
son1 = root.makeelement('son', {'name': '儿1'})
# 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
son2 = root.makeelement('son', {"name": '儿2'})
# 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# grandson2 = ET.Element('grandson', {'name': '儿12'})
grandson2 = son1.makeelement('grandson', {'name': '儿12'})
# 把儿子添加到根节点中
son1.append(grandson1)
son1.append(grandson2)
# 把儿子添加到根节点中
root.append(son1)
root.append(son1)
# 格式化xml
raw_str = prettify(root)
# 写入文件
f = open("xxxoo.xml", 'w', encoding='utf-8')
f.write(raw_str)
f.close()