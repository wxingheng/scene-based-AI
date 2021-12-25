'''
Author: wuxh
Date: 2021-12-05 10:15:37
LastEditTime: 2021-12-05 10:18:37
LastEditors: wuxh
Description: 
FilePath: /基于场景的人工智能综合应用/第二天/练习代码/005.可视化.py
'''
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
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('1')
plt.xlabel('2')
plt.show()


