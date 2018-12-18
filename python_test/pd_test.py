#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zerowin
# @Time    : 2018/12/17


import pandas as pd

df = pd.read_csv("D:\Python_s\Tests/csv/article.csv", delimiter=",", encoding="utf8")

df1 = df.to_csv("D:\Python_s\Tests/csv/article1.csv", columns=['id', 'title'], index=False, header=True)

