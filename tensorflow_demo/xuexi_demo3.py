import tensorflow as tf 


A = tf.Variable(3,name= 'number')
B = tf.Variable([1,3],name='Vector')
C = tf.Variable([[0,1],[1,3]],name = 'matrix')
D = tf.Variable(tf.zeros([100]),name= 'zero')
E = tf.Variable(tf.random_normal([2,3],mean=1 ,stddev=2,dtype=tf.float32))

init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)