''' 
Author: Hao Kang
CPU:
'''

import numpy as np
import time
import math

print('########################第一题#########################')
ans1 = np.float32(9.4) - np.float32(9) - np.float32(0.4)  # Python默认双精度，np.float函数将数据类型强制保存为单精度
ans2 = -13 * math.pow(2, -25)
print("计算结果为：%.12e" % ans1)
print("理论结果为：%.12e" % ans2)

print('########################第二题#########################')

turns = 10 ** 7  #循环次数
a1 = 2
a2 = 2.222222

x = a1
t1 = time.time()
for i in range(turns):
    # 直接计算
    ans = 1 + 2 * x ** 3 + 3 * x ** 7 + 4 * x ** 11 + 5 * x ** 15
t2 = time.time()

t3 = time.time()
for i in range(turns):
    # 优化算法后
    ans = ((((5 * x ** 4 + 4) * x ** 4) + 3) * x ** 4 + 2) * x ** 3 + 1
t4 = time.time()
print("x=2,直接计算多项式所需总时间为：", t2 - t1)
print("x=2,优化算法后计算多项式所需总时间为：", t4 - t3)

x = a2
t1,t2,t3,t4 = 0,0,0,0
t1 = time.time()
for i in range(turns):
    # 直接计算
    ans = 1 + 2 * x ** 3 + 3 * x ** 7 + 4 * x ** 11 + 5 * x ** 15
t2 = time.time()

t3 = time.time()
for i in range(turns):
    # 优化算法后
    ans = ((((5 * x ** 4 + 4) * x ** 4) + 3) * x ** 4 + 2) * x ** 3 + 1
t4 = time.time()
print("x=2.222222,直接计算多项式所需总时间为：", t2 - t1)
print("x=2.222222,优化算法后计算多项式所需总时间为：", t4 - t3)

print('########################第三题#########################')

print('反向迭代：')
I = np.zeros((22, 1))
I[21] = 0
for i in range(21, 0, -1):
    I[i - 1] = (1 / i) * (np.e - I[i])
    print("%.12e" % I[i - 1], i - 1)

print('正向迭代：')
I = np.e - 1
for i in range(1, 22):
    print("%.12e" % I, i - 1)
    I = np.e - i * I
