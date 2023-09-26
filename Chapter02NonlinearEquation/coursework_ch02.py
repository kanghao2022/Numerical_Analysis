#二分法求根
import numpy as np
print("二分法求根")

def f(x):
    y=np.exp(x)+x-7 #输入求根方程的表达式
    return y

a = 1      #区间左端点
b = 2      #区间右端点
e = 1e-9   #精度要求
x0=(a+b)/2 #初始解
iter = 0   #迭代次数

while np.abs(f(x0)-0)>e: #计算方程残差
    if f(a)*f(x0)<0:
        b=x0
    else:
        a=x0
    x0=(a+b)/2
    iter += 1
print("第%2d次迭代的解为%.9f"%(iter,x0))

#不动点迭代求根
import numpy as np
print("不动点迭代求根")
def g(x):        #构造迭代方程
    y=np.log(7-x)
    return y

x0 = 1.5         #初始点
iter = 0
e=1e-9

while(1):
    x1 = g(x0)
    if abs(x1-x0)<e:
        break
    x0=x1
    iter += 1
print("第%2d次迭代的解为%.9f"%(iter,x0))

# 牛顿法迭代
import numpy as np

print("牛顿法迭代求根")


def fun(x):  # 原方程
    y = np.exp(x) + x - 7
    return y


def fun_diff(x):  # 导函数
    y = np.exp(x) + 1
    return y


eps = 1e-9
x0 = 1.5
iter = 0
x = np.zeros(2)
x[0] = x0
x[1] = x0 - fun(x[0]) / fun_diff(x[0])
while np.abs(fun(x[0])) > eps:
    iter += 1
    x[0] = x[1]
    x[1] = x[0] - fun(x[0]) / fun_diff(x[0])
print("第%2d次迭代的解为%.9f" % (iter, x[1]))

# 试位法迭代求根
import numpy as np

print("试位法迭代求根")
a = 1
b = 2
iter = 0
e = 1e-9
while 1:
    c = (b * f(a) - a * f(b)) / (f(a) - f(b))


    if abs(f(c) - 0) < e:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    iter += 1
print("第%2d次迭代的解为%.9f" % (iter, c))

