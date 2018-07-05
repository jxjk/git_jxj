import tensorflow as tf 


random_num = tf.random_normal([2,3],mean = -1,stddev = 4,dtype= tf.float32,seed= None,name = "rnum")
b= tf.zeros_like(random_num,optimize=True)

with tf.Session() as sess:
	print(sess.run (random_num))
	print(sess.run(b))