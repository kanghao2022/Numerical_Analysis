import numpy as np

import numpy as np
def SOR(A,b,itermax,epsilon,omega):
    n = b.shape[0]
    iters = 0
    x_0 = np.zeros((n, ))
    x_hold = x_0 + np.ones((n, ))
    while iters <= itermax:
        x_hold = x_0.copy()
        x_new = x_0.copy()
        for i in range(n):
            x_new[i] = x_0[i] + omega * (b[i] - sum([A[i][j] * x_new[j] for j in range(i)]) - sum(
                [A[i][j] * x_0[j] for j in range(i, n)])) / A[i][i]
            x_0 = x_new.copy()
        error = np.linalg.norm(A@x_hold-b)
        if error < epsilon:
            print('SOR迭代%d次后达到精度.'%iters)
            break
        if iters == itermax:
            print('达到迭代上限')
        iters += 1
    return x_hold


if __name__ == '__main__':
    A = np.array([[3,-1,1],[1,-8,-2],[1,1,5]])
    b = np.array([-2,1,4])


    x = SOR(A,b,100,1e-6,1.075)
    print('解为',x)