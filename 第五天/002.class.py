# '''
# Author: wuxh
# Date: 2021-12-18 15:40:18
# LastEditTime: 2021-12-18 15:40:18
# LastEditors: wuxh
# Description: 
# FilePath: /基于场景的人工智能综合应用/第五天/002.class.py
# '''

class Calculator:
    # 类的初始化函数
    def __init__(self, constant):
        self.pi = 3.1415926
        self.constant = constant
    
    def add(self, a, b):
        return a + b
    
    def compute_perimeter(self, radius):
        return 2 * self.pi * radius
# 初始化一个类
tool = Calculator(constant = 1.0)
# 条用实例上的方法
print(tool.compute_perimeter(radius = 0.5))
print(tool.add(3,4))
