# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description:
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
import numpy as np
from numpy.core.fromnumeric import shape
print(np.__file__)

# 通过list创建矩阵：
x = [1, 2, 3]
a = np.asarray(x)
print(x)
print(a)
print(type(x))
print(type(a))

# 通过arange函数创建矩阵：
a = np.arange(10)  # 默认从0开始到10（不包括10），步长为1
print(a)  # 返回 [0 1 2 3 4 5 6 7 8 9]

a1 = np.arange(5, 10)  # 从5开始到10（不包括10），步长为1
print(a1)  # 返回 [5 6 7 8 9]

a2 = np.arange(5, 20, 2)  # 从5开始到20（不包括20），步长为2
print(a2)  # 返回 [ 5  7  9  11  13  15  17  19]

# 通过linspace创建矩阵：
# linspace()和matlab的linspace很类似，用于创建指定数量等间隔的序列，实际生成一个等差数列。
a = np.linspace(0, 10, 5)  # 生成首位是0，末位是10，含5个数的等差数列
print(a)

# ones,zeros,eye,empty函数创建矩阵：

# ones创建全1矩阵

# zeros创建全0矩阵

# eye创建单位矩阵

# empty创建空矩阵（实际有值）
a_ones = np.ones((3, 4))  # 创建3*4的全1矩阵
print(a_ones)
# 结果
# [[ 1.  1.  1.  1.]
# [ 1.  1.  1.  1.]
# [ 1.  1.  1.  1.]]

a_zeros = np.zeros((3, 4))  # 创建3*4的全0矩阵
print(a_zeros)
# 结果
# [[ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]]

a_eye = np.eye(5)  # 创建5阶单位矩阵
print(a_eye)
# 结果
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

a_empty = np.empty((3, 4))  # 创建3*4的空矩阵
print(a_empty)

# 矩阵的最大值和最小值：
# 获得矩阵中元素最大最小值的函数分别是max和min，可以获得整个矩阵、行或列的最大最小值。
arr = np.array([[1, 2, 11],
                  [4, 5, 8]])

print(arr.max())  # 结果为11
print(arr.min())  # 结果为1
print('===========')
print(arr.mean(axis=0))
# [2.5 3.5 9.5]
print(arr.mean(axis=1))
# [4.66666667 5.66666667]
# print(np.average(arr))

# 同时还可以指定axis关键字，获取行或列的最大、最小值：
# axis=0 每一列
# print(arr.max(axis=0)) #x轴最大值，0,1分别代表行列
# [ 4  5 11]
# axis=0 每一行
# print(arr.max(axis=1)) #x轴最大值，0,1分别代表行列
# [11  8]

# print(np.shape(np.mat()))



# 平均值：
# 获得矩阵中元素的平均值可以通过函数mean()或average()。同样地，可以获得整个矩阵、行或列的平均值：
# array=np.array([[1,2,3],
#                 [4,5,6]])

# # 求矩阵平均值可以如下两个方法：
# print(array.mean())#结果为3.5
# print(np.average(array))#结果为3.5

# # axis = 0  列方向的平均值 [2.5 3.5 4.5]
# print(array.mean(axis=0))#列方向的平均值，同样，0,1代表维度
# # axis = 0  行方向的平均值 [2. 5.]
# print(array.mean(axis=1))#行方向的平均值，同样，0,1代表维度


# a_ones = np.ones((3, 3, 4))  # 创建3*4的全1矩阵
# print(a_ones)
# # 
# # 返回矩阵维度结构
# print(np.shape(a_ones))
# # (3, 3, 4)
# print(a_ones.shape[1])
# 范围指定维度的长度 3

# 结果
# [[[1. 1. 1. 1.]
#   [1. 1. 1. 1.]]]