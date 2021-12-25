# '''
# Author: wuxh
# Date: 2021-12-25 11:19:06
# LastEditTime: 2021-12-25 11:19:06
# LastEditors: wuxh
# Description:
# FilePath: /基于场景的人工智能综合应用/第七天/001.py
# '''
import matplotlib.pyplot as plt  # 导入matplotlib用于绘图
import jieba  # 分词
import wordcloud  # 词云
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np  # 生成词云
from PIL import Image  # 读取背景图片

old_file = '/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第七天/data/002.txt'  # 读取文件

# 读取文件
with open(old_file, 'r', encoding='utf-8') as f:  # 打开文件
    text = f.read()  # 读取文件
# print('========', text)
new_text = jieba.cut(text, cut_all=False)  # 分词
str_out = ' '.join(new_text)  # 将数组转换成字符串
str_out = str_out.replace('，', '').replace('；', '').replace('。', '').replace(
    '？', '').replace('！', '').replace('：', '').replace('\n', '')  # 去除标点符号
# print('str_out=====++++===', str_out)

background = np.array(Image.open( # 读取背景图片
    '/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第七天/data/005.png'))  # 读取背景图片
wc = WordCloud(width=1400, height=2200,  # 设置图片大小
               background_color='white',
               mode='RGBA',  # 设置图片模式
               mask=background,  # 添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
               max_words=500,  # 设置最大显示的字数
               stopwords=STOPWORDS.add(''),  # 内置的屏蔽词,并添加自己设置的词语
               # font_path='/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第七天/data/simhei.ttf',
               # font_path='C:\Windows\Fonts\STZHONGS.ttf',
               font_path='/System/Library/fonts/PingFang.ttc',  # 设置字体
               max_font_size=200,  # 设置字体最大值
               relative_scaling=0.6,  # 设置字体大小与词频的关联程度为0.4
               random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
               scale=2  # 设置生成词云图片的大小
               ).generate(str_out)  # 生成词云

image_color = ImageColorGenerator(background)  # 设置生成词云的颜色，如去掉这两行则字体为默认颜色
wc.recolor(color_func=image_color)  # 将图片颜色设置为背景图片的颜色

plt.figure(figsize=(10, 20))  # 设置图片大小
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭x,y轴
# plt.show()#显示
wc.to_file(
    '/Users/wuxh/coder/github/example/python/基于场景的人工智能综合应用/第七天/data/cloud-output.jpg')  # 保存词云图
