import numpy as np

def GS(A,b,itermax,epsilon):
    n = b.shape[0]
    x0 = np.zeros((n,))                      #初始化迭代点
    x = np.zeros((n,))                       #初始化迭代点
    iters = 0                                               #初始化计数器
    while iters <= itermax:                                        #开始迭代
        for i in range(n):                                 
            temp = 0
            xtemp = x0.copy()
            for j in range(n):
                if i != j:
                    temp += x0[j] * A[i][j]            #求和
            x[i] = (b[i] - temp) / A[i][i]
            x0[i] = x[i].copy()
        error = np.linalg.norm(A@x-b)
        if error < epsilon:
            print('Gauss_Seidal迭代%d次后达到精度.'%iters)
            break
        if iters == itermax:
            print('达到迭代上限')
        iters += 1
    return x


if __name__ == "__main__":

    A = np.array([[3,-1,1],[1,-8,-2],[1,1,5]])
    b = np.array([-2,1,4])

    x = G_S(A,b,20,1e-6)
    print('解为',x)