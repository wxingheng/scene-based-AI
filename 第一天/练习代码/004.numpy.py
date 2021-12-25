# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description:
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
import numpy as np

x = [3, 7, 9, 3, 4, 5, 2, 1, 6, 8]
print(type(x), x)
x = np.array(x)
print(type(x), x)
print(x.shape, x.dtype)
# 三行四列 1
print(np.ones((3, 4)))
# 三行四列 0
print(np.zeros((3, 4)))
# 三行四列  0 ～ 1 随机
print(np.random.rand(3,4))
# 三行四列  -1 ～ 1 随机
print(np.random.randn(3,4))
# 三行四列  1 ～ 10 随机整数
print(np.random.randint(1, 10, size=(3, 4)))
# 四行四列 对角线函数
print(np.eye(4,4))

test_array= np.random.rand(5)
print(test_array)
print(np.sort(test_array))
print(np.argsort(test_array))
# print(np.poly(test_array))

# 二维数组的操作
test_array =  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('===', np.max(test_array, axis=0))
print('===', np.max(test_array, axis=1))


# 数组切片
# 第一列的所有行
print(test_array[1:2, 1:2])

# 相乘
x1 = np.random.randint(low=1, high=10, size=(3))
x2 = np.random.randint(low=1, high=10, size=(3))
print(x1 * x2)




# print(np.__file__)

# a=np.array([[1,3,5,7],[2,4,6,8]])
# 2 (2, 4) 8 int64
# print(a.ndim, a.shape, a.size, a.dtype)
