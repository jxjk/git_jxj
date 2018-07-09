from numpy import *
import os


a = arange(12).reshape(3,4)
print(a)
# [[ 0 1 2 3]
#  [ 4 5 6 7]
#  [8 9 10 11]]


# 创建一个和a相同的数组b
b = a.copy()
c = a.ravel()
d = b.flatten()

# 输出c和d数组
print(c)
# [ 0 1 2 3 4 5 6 7 8 9 10 11]
print(d)
# [ 0 1 2 3 4 5 6 7 8 9 10 11]
# 可以看到c和d数组都是扁平化后的数组，具有相同的内容

print(a is c)
# False
print(b is d)
# False
# 可以看到以上a,b,c,d是四个不同的对象

# 但因为c是a的一种展示方式，虽然他们是不同的对象，但在修改c的时候，a中相应的数也会改变。
c[1] = 99
d[1] = 99
print(a)
# [[ 0 99 2 3]
#  [ 4 5 6 7]
#  [8 9 10 11]]

print(b)
# [[ 0 1 2 3]
#  [ 4 5 6 7]
#  [8 9 10 11]]

print(c)
# [ 0 99 2 3 4 5 6 7 8 9 10 11]
print(d)
# [ 0 99 2 3 4 5 6 7 8 9 10 11]

os.system("pause")
