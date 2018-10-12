#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zerowin
# @Time    : 2018/9/4

import time


# 函数作用
# 1、减少重复代码
# 2、方法修改，易于扩展
# 3、保持代码一致性

# 不能用python保留字
# 调用一定要加括号

def f():
    print('function 1')


f()


# 参数
def add(a, b):
    print(a + b)


# 按顺序分配参数
add(5, 7)


def logger(n):
    time_format = '%Y-%m-%d %x'
    time_current = time.strftime(time_format)

    with open('日志记录', 'a')as f:
        f.write('%s end action%s\n' % (time_current, n))


def action1(n):
    print('starting action1...')
    # with open('日志记录', 'a')as f:
    #     f.write('ending action1...''\r')
    logger(n)


def action2(n):
    print('starting action2...')
    # with open('日志记录', 'a')as f:
    #     f.write('ending action2...''\r')
    logger(n)


def action3(n):
    print('starting action3...')
    # with open('日志记录', 'a')as f:
    #     f.write('ending action3...''\r')
    logger(n)


action1(11)

action2(22)

action3(33)


# 打印信息
# 默认参数
def print_info(name, age, sex='male'):
    print('Name: %s' % name)
    print('Age: %d' % age)
    print('Sex: %s' % sex)


# 必须参数
# print_info(39, 'xiaohu')
print_info('xiaohu', 19)  # 必须参数
# 关键字参数
print_info(age=29, name='xiaohu')
print_info('lichun', 22, 'female')
