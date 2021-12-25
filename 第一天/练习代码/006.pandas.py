# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description:
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
# Pandas 是 Python 的核心数据分析支持库，提供了快速、灵活、明确的数据结构，旨在简单、直观地处理关系型、标记型数据。

# Pandas 适用于处理以下类型的数据：

# 与SQL或Excel表类似的，含异构列的表格数据;
# 有序和无序（非固定频率）的时间序列数据;
# 带行列标签的矩阵数据，包括同构或异构型数据;
# 任意其它形式的观测、统计数据集, 数据转入 Pandas 数据结构时不必事先标记。
# pandas基本数据结构：

# 目前，pandas的基本数据结构有3种，Series,DataFrame和Pandel。

# 要想熟练使用Pandas,这三种数据结构一定要牢记于心。

# 其中DataFrame使用频率最高。

import pandas as pd
import os
import sys
# path = os.getcwd()
# print(path)
# print(sys.path.append("/home/a/"))
# df = pd.read_csv(path + ".\第一天\练习代码\006.csv")

# df = pd.read_csv("006.csv")
df = pd.read_csv("/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第一天/练习代码/info.csv")
print(df)
# 查看dataframe的信息:
print(df.info())        # 数据类型，内存消耗等信息
print(df.describe() )   # 统计特征，均值方差等

# # 排序操作：
# # 对数据进行排序，用到了sort_values，by参数可以指定根据哪一列数据进行排序，ascending是设置升序和降序。
# print(df.sort_values(by = 'dn2', ascending = True))

# print(df.loc[:2])       # 选取了前三行，想想和list的索引有何区别？
# print(df.loc[:, 'dn3'])# 选取‘name'列所有的数据
# print(df.loc[3:5, 'tid':'dn2']) # 是否选取了name和gender两列数据？
# # 以下这条语句：

# print(df.loc[:, 'name':'gender'] )
df.loc[:]        # 选取整个表格，想想为什么？
df.loc[:2]       # 选取了前三行，想想和list的索引有何区别？
df.loc[:, 'name']# 选取‘name'列所有的数据

# print(df.loc[:, 'name':'gender']) # 是否选取了name和gender两列数据？
# 所有行 ，指定'name':'gender'列
print(df.loc[ :, 'name':'gender']) # 是否选取了name和gender两列数据？

# 是选取了从'name'到’gender‘的所有列，而不是只选择了'name'和’gender‘。
# print(df.sort_values(by = 'age', ascending = False))

# # 如何解决loc只能连续选取的问题？
# print(pd.DataFrame(df, columns=['gender', 'name']))

# # pandas总结：

# # pandas相当于使用Python操作Excel
# # 所有Excel的操作都可以在pandas中找到对应操作