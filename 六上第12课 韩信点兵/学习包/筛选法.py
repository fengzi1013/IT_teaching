# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/16 16:53
@Auth ： fengzi
@File ：筛选法.py
@IDE ：PyCharm
@Describe:  # 先删选大的数。7，5,3的顺序，次数最优
"""
n = 1  # n为记录运行次数的变量
a =  [i for i in range(1000, 1101)] # 储存满足条件的数
a1 = a.copy()
# 删除不满除以7余数为2的数
for k in a1:
    if k % 7 != 2:
        a.remove(k)
    n += 1
# 删除不满除以5余数为5的数
a1 = a.copy()
for i in a1:
    if i % 5 != 3:
        a.remove(i)
    n += 1
# 删除不满除以3余数为2的数
a1 = a.copy()
for j in a1:
    if j % 3 != 2:
        a.remove(j)
    n += 1

print("剩余的士兵数量：",a)
print("运行次数：", n)
