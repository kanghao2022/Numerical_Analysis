#################################  Main code #####################################
import numpy as np
def Gauss(A, b):
    ''' 
    定义函数Gauss(A,b)
    Input:
    系数矩阵A: type = array 需要求解的方程组的系数矩阵
    常数矩阵b: type = array 需要求解的方程组的常数列
    Output:
    xi:    type = array(i = 1,2,……,n) 方程组的解向量
    '''
    #initialization
    A = A.copy()
    b = b.copy()
    m,n = A.shape                                       
    if m != n:                                          
        return 'No unique solution'                           
    x = np.zeros(n)                                     
    l = np.zeros((n,n))                                 
    #elimination
    for k in range(n - 1):                              
        if A[k][k] == 0:                                
            return 'Error Input'                        
        for i in range(k+1,n):                          
            l[i][k] = A[i][k] / A[k][k]                 
            for j in range(n):                          
                A[i][j] = A[i][j] - l[i][k] * A[k][j]   
            b[i] = b[i] - l[i][k] * b[k]                
        #print(A)                                       
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]               
    #recursive
    for i in range(n - 2, -1, -1):                      
        for j in range(i + 1, n):                       
            b[i] -= A[i][j] * x[j]                      
        x[i] = b[i] / A[i][i]                        
    x = x.reshape(n,)
    return x

###################################  Test  code #####################################
if __name__ == '__main__':
    A = np.array([[3,1,2], [6, 3 ,4], [3, 2, 5]])
    b = np.array([11,24,22])
    x = Gauss(A, b)
    print("解为",x)
    print("Gauss消去计算方程组的残差的2范数为：",np.linalg.norm(A@x-b))
    print("解为",x)
    print("LU分解计算方程组的残差的2范数为：",np.linalg.norm(A@x-b))