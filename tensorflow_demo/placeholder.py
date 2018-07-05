import numpy as np 
import tensorflow as tf 


#x = tf.placeholder(dtype = tf.float32,shape=(1024,1024))
x = tf.placeholder(dtype = tf.float32,shape=(None,None)) # None 表示任意维度
y = tf.matmul(x,x)

with tf.Session() as sess:
	#print(sess.run(y)) # ERROR: will fail because x was not fed.

	#rand_array = np.random.rand(1024,1024)
	rand_array = np.random.rand(2,2)
	print(sess.run(y,feed_dict={x: rand_array})) # will succeed. 