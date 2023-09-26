import numpy as np

def Jacobi(A,b,itermax,epsilon):
    n = b.shape[0]
    x = np.zeros((n,))
    iters = 0
    while iters <= itermax:
        for i in range(n):
            temp = 0
            for j in range(n):
                if j != i:
                    temp += A[i,j]*x[j]
            x[i] = (b[i] - temp)/A[i,i]
        error = np.linalg.norm(A@x-b)
        if error < epsilon:
            print('Jacobi迭代%d次后达到精度.'%iters)
            break
        if iters == itermax:
            print('达到迭代上限')
        iters += 1
    return x

if __name__ == '__main__':
    A = np.array([[3,-1,1],[1,-8,-2],[1,1,5]])
    b = np.array([-2,1,4])


    x = Jacobi(A,b,20,1e-6)
    print('解为',x)