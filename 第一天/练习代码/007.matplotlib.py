# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description:
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
# matplotlib是python中常用的图表绘制工具。
# 绘制简单折线图：

# 可以直接使用plt.plot函数。

# 其中，第一个参数是横轴对应数据，第二个参数是纵轴对应数据。

# import matplotlib.pyplot as plt
# import pandas as pd

# plt.title("GDP of China from 2015 to 2019")
# plt.plot(range(2015,2020,1), [11.06, 11.23, 12.31, 13.89, 14.28])
# plt.show()

# df = pd.read_csv("/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第一天/练习代码/006.csv")

# df_age_ascend = df.sort_values(by = 'id', ascending = True)   # 先新建一个表格，这个表格按照年龄升序排列
# print(df_age_ascend)
# plt.plot(df_age_ascend['id'], df_age_ascend['dn3'])
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))
x = np.linspace(start=-5, stop = 5, num=100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin', marker='*')
plt.plot(x, y_cos, label='cos', marker='o')
plt.grid(True)
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.title('A sample example', fontsize = 20)
plt.legend(fontsize=15)

plt.show()


# plt.plot(range(2015,2020,1), [11.06, 11.23, 12.31, 13.89, 14.28])
# plt.show()