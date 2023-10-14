import numpy as np

# def Jacobi(A,b,itermax,epsilon):
#     n = b.shape[0]
#     x = np.zeros((n,))
#     iters = 0
#     while iters <= itermax:
#         for i in range(n):
#             temp = 0
#             for j in range(n):
#                 if j != i:
#                     temp += A[i,j]*x[j]
#             x[i] = (b[i] - temp)/A[i,i]
#         error = np.linalg.norm(A@x-b)
#         if error < epsilon:
#             print('Jacobi迭代%d次后达到精度.'%iters)
#             break
#         if iters == itermax:
#             print('达到迭代上限')
#         iters += 1
#     return x
def Jacobi(A,b,k,epsilon):#k迭代次数
    m,n=A.shape
    X=np.zeros(n)#初次迭代X[0,0,0]
    x=np.zeros(n)#迭代后更新x
    times = 0
    while times<k:
        for i in range(n):
            sum=0
            for j in range(n):
                if(i!=j):
                  sum=sum+A[i][j]*X[j]
            x[i]=(b[i]-sum)/A[i][i]
        X=x.copy()
        error = np.linalg.norm(A@X-b)
        if error < epsilon:
            print('Jacobi迭代%d次后达到精度.'%times)
            break
        times=times+1
          #迭代X
    return X

if __name__ == '__main__':
    # A = np.array([[3,-1,1],[1,-8,-2],[1,1,5]])
    # b = np.array([-2,1,4])


    # x = Jacobi(A,b,20,1e-6)
    # print('解为',x)
    import scipy.io as sio
    import numpy as np
    from scipy.sparse import csr_matrix

    n = 10
    with open('F:\PycharmFile\MyProject\Test_100.txt', 'r') as f:
        # open为打开文件，r为读取
        f = open('F:\PycharmFile\MyProject\Test_100.txt', 'r')
        # 逐行读取文件内容
        lines = f.readlines()
        rowOffSet = []
        m_colIndex = []
        m_value = []
        for j in range(len(lines)):
            temp_strLst = lines[j].split()
            # print(temp_strLst)
            for i in range(2, len(temp_strLst)):
                if j == 0:
                    rowOffSet.append(eval(temp_strLst[i]))
                if j == 1:
                    m_colIndex.append(eval(temp_strLst[i]))
                if j == 2:
                    m_value.append(eval(temp_strLst[i]))
        f.close()


    indptr = np.array(rowOffSet)
    indices = np.array(m_colIndex)
    data = np.array(m_value)
    A = csr_matrix((data, indices, indptr), shape=(n ** 2, n ** 2), dtype=float)

    with open('F:\PycharmFile\MyProject\TestArray_100.txt', 'r') as f:
        # open为打开文件，r为读取
        f = open('F:\PycharmFile\MyProject\TestArray_100.txt', 'r')
        # 逐行读取文件内容
        lines = f.readlines()
        rightHandsideArray = []
        temp_strLst = lines[0].split()

        for i in range(2, len(temp_strLst)):
            rightHandsideArray.append(eval(temp_strLst[i]))
        f.close()
        b = np.array(rightHandsideArray)
    
    A = A.toarray()
    x1= Jacobi(A,b,1000,1e-6)