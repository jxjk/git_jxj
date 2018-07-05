import tensorflow as tf
import numpy as np


# 创建数据
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# 搭建模型
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

# 计算误差
loss = tf.reduce_mean(tf.square(y - y_data))

# 反向传播误差
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 训练&保存
saver = tf.train.Saver({"Weights":Weights,"biases":biases})

## Save to file
# remember to define the same dtype and shape when restore
W = tf.Variable([[1,2,3],[3,4,5]], dtype=tf.float32, name='weights')
b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases))

save_path = saver.save(sess,"my_net/save_net.ckpt")
print("Save to path",save_path)
