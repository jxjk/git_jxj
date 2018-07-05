import tensorflow as tf


hello = tf.constant('Hello,TensorFlow!')
a = tf.constant(10)
b = tf.constant(32)

with tf.Session() as sess:
    print(sess.run(hello))
    print(sess.run(a+b))

     
