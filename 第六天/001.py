
# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''

import cv2
import matplotlib.pylab as plt
import numpy as np

# img = cv2.imread('./002.png')
# img = cv2.imread(r'/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第六天/001.jpeg', 1)
img = cv2.imread(r'/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第六天/002.png', 1)
# plt.imshow(img)



print(type(img))

def translate(img, x, y):
    (h, w) = img.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted_img = cv2.warpAffine(img, M, (w, h))
    return shifted_img

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (3000, 3000))
# new_img = translate(img, x=50, y=50)
cv2.imshow('222', img)
cv2.waitKey()
cv2.destroyAllWindows()


