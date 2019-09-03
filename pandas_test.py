#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-03 10:36
# @Author  : liupan
# @Site    : 
# @File    : pandas_test.py.py
# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt

stu_df3 = pd.DataFrame({
    '语文': [40, 70, 65, 45],
    '数学': [50, 86, 56, 78],
    '英语': [79, 96, 87, 54]
},
    index=['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    columns=['语文', '数学']
)
print(stu_df3)
stu_df3.plot.bar(rot=0, title="student's score")
plt.show()
