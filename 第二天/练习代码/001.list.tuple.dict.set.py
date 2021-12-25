# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''

# list 内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'B·ob', 'Tracy']
print(classmates)
c = classmates.pop()
print(classmates, c)



# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmatestuple = ('Michael', 'Bob', 'Tracy')
print(classmatestuple)
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。


# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
ran = range(5)
print(ran)
print(list(ran))

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
print(d)
print(d['Bob'])


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3, 2])
print(s)
print(list(s))
print(list(range(1, 5, 1)))

# print(set([  {'name': 22} ]))
# TypeError: unhashable type: 'dict'

# example_list = [1]

# print(example_list)

# list_of_list = [[1,2,3], [6,7,8]]

# three = list_of_list[0][2]

# my_list = [i for i in range(10)]
# print(my_list)

# my_list2 = [i**2 for i in range(10)]
# print(my_list2)

# my_list3 = [[i + j for i in range(5)] for j in range(10)]
# print(my_list3)
# # 双层循环，第一层循环10次，第二层循环5次
# # [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13]]



# random_list = [3,12,5,6]
# sorted_list = sorted(random_list)


# random_list = [(3, 'A'), (12, 'D'),(5, 'C')]
# print(random_list)
# # [(3, 'A'), (12, 'D'), (5, 'C')]

# sorted_list = sorted(random_list)


# l = ['A', 'B', 'C', 'B']
# print(l)
# l.append('444')
# l.insert(3,'444')
# l.append([3,4,5]) 
# l.append((333, 555)) 
# l.append({22:33}) 
# print(l)
# print(
#     '''
#     line1
# ... line2
# ... line3
#     '''
#     )


# # r 标识默认不转译， 这就打印结果就是 
# print(r'''hello,\n world''')
# # hello,\n world

# print('''hello,\n world 你好，世界''')
# # 没有r会自动换行
# # hello,
# # world

# print('你好 python')


