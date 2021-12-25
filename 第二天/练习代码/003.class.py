# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
# 面对对象编程
class Vericle:
    def __init__(self, make, name, year, is_electric=False, price=100):
        self.name = name
        self.make = make
        self.year = year
        self.is_electric = is_electric
        self.price = price
        
        self.odometer = 1
        
    def drive(self, distance):
        self.odometer += distance
        
    def compute_price(self):
        # price = 0
        if self.is_electric:
            price = self.price / (self.odometer * 0.8)
        else:
            if self.odometer == 0:
                print("error: 除数不能为0")
            else:
                price = self.price / self.odometer
        return price
    
    
if __name__ == '__main__':
    family_car = Vericle('Honda', 'Accord', '2019', price=1000)
    print(family_car.compute_price())
    family_car.drive(100)
    print(family_car.compute_price())
    