#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zerowin
# @Time    : 2018/9/4

import copy
# 浅copy只copy一层  深copy=copy一份
a = [[1, 2], 3, 4]

b = a.copy()
b[0][0] = 121
print(a)
print(b)
print(a)

a1 = [[1, 2], 3, 4]
c = a.copy()
c[0][0] = 121
print(a1)
print(c)
print(a1)


husband = ["zerowin", 123, [15000, 9000]]

wife = husband.copy()
wife[0] = "xiaoqiao"
wife[1] = 124

gfriend = copy.deepcopy(husband)
gfriend[0] = "daqiao"
gfriend[1] = 666
gfriend[2][1] -=1999

print(wife)
print(gfriend)

