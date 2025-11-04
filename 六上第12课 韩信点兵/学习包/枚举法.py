# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/16 16:14
@Auth ： fengzi
@File ：枚举法.py
@IDE ：PyCharm
@Describe:
"""

n = 1  # n为记录运行次数的变量
x= 1000
while x< 1101:
    if x%3==2 and x%5==3 and x%7==2:
        print("剩余的士兵数量：",x)
        print("运行次数：", n)
    x += 1
    n += 1
