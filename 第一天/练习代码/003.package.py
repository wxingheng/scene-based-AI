# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
import random
import time
# 0-1 的随机数
print(random.random())

# 4 - 10 的随机整数 randint接受指定范围
print(random.randint(4,10))

# choice 接受有序序列
print(random.choice(range(4,10)))

# 睡眠时间 单位 秒
time.sleep(1)
#时间转化为字符串
print(time.ctime())
#时间转化为 struct_time
print(time.localtime())

#时间format
print(time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime()))

# sample  获取指定range中的指定长度
print(random.sample(range(4,10), 2))

