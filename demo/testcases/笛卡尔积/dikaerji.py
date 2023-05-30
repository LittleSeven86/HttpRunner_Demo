#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :dikaerji.py
    @Time      :2023/5/27 13:32
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
import itertools
# 定义要计算笛卡尔积的列表
list1 = [1, 2, 3]
list2 = ['a', 'b']
list3 = ['x', 'y', 'z']
# 计算列表的笛卡尔积
cartesian_product = list(itertools.product(list1, list2, list3))
# 输出结果
print(cartesian_product)

