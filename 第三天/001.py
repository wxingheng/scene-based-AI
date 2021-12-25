# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
# import numpy as np;
# data = np.array([[1,2,3],[4,5,6]]);
# print(data.max());
# # 新建一个二维矩阵，长度为20，宽度为3
# d = np.zeros((20,3));
# # 新建一个array [1 2 3 4 5]
# arr = np.array([1,2,3,4,5]);
# # 新建一个list [1, 2, 3, 4, 5]
# l = [1,2,3,4,5];
# print(arr, l);
# # array 转 list 方法
# # def arrToList(arr):
#     # return list(arr);
# print(arr[0:2]);
# print(arr.sum());
# print(np.array([[[1,2],[3,4]],[[5,6],[7,8]]]));
# print(np.array(1,2,3).dot())
import numpy as np;
data = np.array([[1,2],[3,4], [5,6]]);
print('data===>', data)
print('data[0,1]===>', data[0,1])
print(data[1:3])
print(data[0:2,0])
print(data.T)

data = np.array([1,2,3,4,5,6]);
print('data===>', data)
print('data.reshape(2,3)===>', data.reshape(2,3))
print('data.reshape(3,2)===>', data.reshape(3,2))






