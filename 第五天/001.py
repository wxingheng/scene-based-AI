# '''
# Author: wuxh
# Date: 2021-12-18 14:51:03
# LastEditTime: 2021-12-18 14:51:03
# LastEditors: wuxh
# Description:
# FilePath: /基于场景的人工智能综合应用/第五天/001.py
# '''

tuple_a = (1, 2)
list_a = [1, 2, 3, 4]

try:
    tuple_a[0] = 3
except:
    print('----')

for i in range(5):
    print(i)
print('\n')

for item in list_a:
    print(item)


for idx, item in enumerate(list_a):
    if idx == 1:
        # continue
        break
    else:
        print(idx, item)


list_b = [3, 4, 2, 1, 5, 6, 7]
# 冒泡排序
def dobule_sorting(list):
    # 获取数组长度
    length = len(list)
    # 记录共循环了多少次
    count = 0
    # 外层循环，控制趟数，每一次找到一个最大值
    for i in range(length):
        # 内层循环,控制比较的次数，并且判断两个数的大小
        for j in range(length - i - 1):
            # 白话解释：如果左边的数大，放到右边(当然是从小到大的冒泡排序)
            if list[j] > list[j + 1]:
                t = list[j]
                list[j] = list[j + 1]
                list[j + 1] = t
            count = count + 1
    return list, count

print(dobule_sorting(list_b))
