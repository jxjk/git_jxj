import tensorflow as tf 


a = tf.constant([[2.0,3.0]],name = 'a')
b = tf.constant([[1.0],[4.0]],name = 'b')

result = tf.matmul(a,b,name = "mul")

print(result)
with tf.Session() as sess:
	print(sess.run(result))