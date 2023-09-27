# LU分解
import numpy as np
def LU_Doolittle_decomp(A,b):
    ''' 
    定义函数LU(A,b)
    Input:
    系数矩阵A: type = array 需要求解的方程组的系数矩阵
    常数矩阵b: type = array 需要求解的方程组的常数列
    Output:
    xi:    type = array(i = 1,2,……,n) 方程组的解向量
    '''
    A = A.copy()
    b = b.copy()
    n,m = A.shape[0],A.shape[1]
    y = np.zeros((n,1))
    x = np.zeros((n,1))

    if n != m:
        return 'error dimension'
    L = np.eye(n)
    U = np.zeros((n,n))
    U[0,:] = A[0,:]
    for i in range(n):
        L[i,0] = A[i,0]/U[0,0]
    for i in range(1,n):
        for j in range(i,n):
            U[i,j] = A[i,j] - np.dot(L[i,:i],U[:i,j])
            if(j+1<n):
                L[j+1,i] = (A[j+1,j] - np.dot(L[j+1,:i],U[:i,i]))/U[i,i]
    # print(L)
    # print(U)
    
    #向前回代求解Ly=b
    y[0] = b[0]/L[0,0]
    for i in range(1,n):
        for j in range(i):
            b[i] = b[i] - L[i,j]*y[j]
        y[i] = b[i]/L[i,i]

    #向前回代求解Ux=y
    x[n-1] = y[n-1]/U[n-1,n-1]
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            y[i] = y[i] - U[i,j]*x[j]
        x[i] = y[i]/U[i,i]
    x = x.reshape(n,)

    return x

def LU_Doolittle_decomp_Matrix(A):
    n,m = A.shape[0],A.shape[1]

    if n != m:
        return 'error dimension'
    L = np.eye(n)
    U = np.zeros((n,n))
    U[0,:] = A[0,:]
    for i in range(n):
        L[i,0] = A[i,0]/U[0,0]
    for i in range(1,n):
        for j in range(i,n):
            U[i,j] = A[i,j] - np.dot(L[i,:i],U[:i,j])
            if(j+1<n):
                L[j+1,i] = (A[j+1,j] - np.dot(L[j+1,:i],U[:i,i]))/U[i,i]

    return L,U

# if __name__ == '__main__':
#     A = np.array([[3,1,2], [6, 3 ,4], [3, 2, 5]])
#     L,U=LU_Doolittle_decomp_Matrix(A)
#     print(L)
#     print(U)
#     print(np.matmul(L,U))

if __name__ == '__main__':
    A = np.array([[3,1,2], [6, 3 ,4], [3, 2, 5]])
    b = np.array([11,24,22])
    x = LU_Doolittle_decomp(A,b)
    print("解为",x)
    print("LU分解计算方程组的残差为：",np.linalg.norm(A@x-b))