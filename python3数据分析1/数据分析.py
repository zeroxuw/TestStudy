#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zerowin
# @Time    : 2018/12/18

# json: 字典转化为json文本,json文本转化为字典
# pandas可以给每行或每列为索引取名字
# Numpy是一个python数据分析的library，core为C语言完成

import numpy as np

# 用np.array初始化数组
a = np.array([1, 2, 3])
print(a)
print(type(a))
print(type([1, 2, 3]))
print(a)

# 二维数组
b = np.array([[1, 2, 3], [2, 3, 4]])
print(b)
# 矩阵n*m(2行3列)
print(b.shape)
# b数组1行2列
print(b[0, 1])

# 2行3列0数组
c = np.zeros((2, 3))
print(c)
# 2行3列1数组
d = np.ones((2, 3))
print(d)
# 2行3列8数组
e = np.full((2, 3), 8)
print(e)
# 对角矩阵
f = np.eye(3)
print(f)
# 0-1随机数组
g = np.random.random((3, 2))
print(g)
# 任何数数组
h = np.empty((2, 4, 3))
print(h)
arr = np.array([1, 2, 3])
print(arr.dtype)
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr.dtype)
# 使用astype复制数组并转换数据类型
int_arr = np.array([1,2,3,4,5])
print(int_arr, int_arr.dtype)
float_arr = int_arr.astype(np.float64)
print(float_arr, float_arr.dtype)


