# '''
# Author: wuxh
# Date: 2021-12-25 11:19:06
# LastEditTime: 2021-12-25 11:19:06
# LastEditors: wuxh
# Description: 
# FilePath: /基于场景的人工智能综合应用/第七天/001.py
# '''
import matplotlib.pyplot as plt # 导入matplotlib用于绘图
import jieba # 分词
import wordcloud #  词云
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np # 生成词云
from PIL import Image # 读取背景图片

old_file = '/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第七天/data/滕王阁序.txt' # 读取文件

# 读取文件
with open(old_file, 'r', encoding='utf-8') as f: # 打开文件
    text = f.read() # 读取文件
print('========', text)
new_text = jieba.cut(text, cut_all = False)# 分词
str_out = ' '.join(new_text) # 将数组转换成字符串
str_out = str_out.replace('，', '').replace('；', '').replace('。', '').replace('？', '').replace('！', '').replace('：', '').replace('\n', '') # 去除标点符号
print('str_out=====++++===', str_out)