#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zerowin
# @Time    : 2018/12/16


# 第一章 python基础
# python有六大数据类型：number(数字)、string(字符串)、list(列表)、tuple(元组)、sets(集合)、dictionary(字典)
# 四种数字类型：int(整数类型)、float(浮点类型)、bool(布尔类型)、complex(复数类型)
# 原始字符串通过给字符串加上前缀r或R的方式指定
print(r"Newlines are indicated by \n")
# 字符串截取为"左闭右开"
# python列表是任意对象(列表嵌套列表或字符串)的有序集合，列表写在中括号[]内，元素之间用逗号隔开
# 列表切片 print(list[0])
# 列表删除 list.remove(2)
# 元组与列表类似，区别在于元组的元素不能修改，元组写在小括号()内，元组之间用逗号隔开
tuple0 = [1, "zero", 8859_1, "8859_1", 'win', "python"]
tuple1 = (1, "zero", 8859_1, "8859_1", 'win', "python")
print(tuple0[0:5])
print(tuple1[0:5])
# 集合是一个无序不重复元素的序列，可以使用大括号{}或set()函数创建，空集必须使用set()函数创建而不能使用大括号{}，
# 因为大括号{}是用来创建字典的。
# 字典是一种可变容器模型，可以存储任意类型对象，用{}标识。字典是一个无序的键(key)值(value)对集合
information = {'name': 'liming', 'age': '24', 'sex': 'boy'}
print(information)
# 用del函数删除字典数据
del information['age']
print(information)
# 条件语句 循环语句
sum = 0
for i in range(1, 10, 1):
    sum = i + sum
print(sum)


# range函数：i从1(第一个参数)开始迭代，每次加1(第三个参数)，直到i变成了10(第二个参数)结束，i=10时不执行，循环9次
# 内建函数：可以直接调用，如print()、int()  外建函数：即自定义函数
def f(x):
    y = 5 * x + 2
    return y


# 第二章 写一个简单的爬虫
