#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

# 1.abs()求绝对值
print(abs(-100))

# 2.all()只要每个元素都为真才返回真，假为：0 False None "" [] {}即为假
print(all([True, True]))

# 3.any()只要其中一个为真，结果为真
print(any([False, True, False]))

# 4.ascii(对象)从对象的类中找__repr__方法，并获取返回值
class Foo:
    def __repr__(self):
        return "hello wrold"

print(ascii(Foo()))


# 5.bin()十进制转二进制
print(bin(100))

# 6.oct()十进制转八进制
print(oct(100))

# 7.hex()十进制转十六进制
print(hex(100))

# 8.int()二进制、八进制、十进制、十六进制转十进制
print(int(0b1100100))
print(int(0o144))
print(int(0x64))
print(int('0b1100100', base=2))         #base表示当前字符串的进制，这里的作用是将二进制的字符串转成十进制


# 9.bool()判断bool类型
print(bool(None))


# 10.bytes()字符串转字节
print(bytes('傻逼', encoding='utf-8'))

# 10.bytearray()多种用法
print(bytearray([1, 2, 3, 4]))
print(bytearray('傻逼', encoding='utf-8'))
print(bytearray(4))
print(bytearray())

# 11.chr()返回对应ascii码的字符
print(chr(64))

# 12.ord()返回对应字符的ascii码
print(ord('a'))

# callable() 是否可执行
def func1():
    print("傻逼了")

print(callable(func1))
print(callable(123))
