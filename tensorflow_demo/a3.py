import tensorflow as tf


mattrix1 = tf.constant([[3.,3.]])
mattrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(mattrix1,mattrix2)
with tf.Session() as sess:
    with tf.device("/gpu:1"):
        result = sess.run (product)
        print(result)
"""
with tf.Session() as sess:
    result = sess.run (product)
    print(result)
"""
