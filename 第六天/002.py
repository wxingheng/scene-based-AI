# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''
import tensorflow as tf

input_tensor = tf.keras.Input(shape=[1, ])
output_tensor = tf.keras.layers.Dense(1)(input_tensor)
model = tf.keras.Model(input_tensor, output_tensor)
model.summary()
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    loss=tf.keras.losses.MeanSquaredError()
)

import numpy as np
import matplotlib.pyplot as plt

w = 2.0
b = 1.5

x = np.linspace(-5, 5, 128)
y = w * x + b
y = y + np.random.randn(128)

model.fit(x, y, batch_size=16, epochs=50)
pred_y = model.predict(x)

plt.scatter(x ,y)
plt.grid(True)
plt.show()