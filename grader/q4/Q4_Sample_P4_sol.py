import numpy as np

def read_matrix():
    r,c = [int(e) for e in input().split()]
    m = [[int(e) for e in input().split()] for i in range(r)]
    return np.array(m)

def dot_row_column(m):
    p = np.zeros_like(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            p[i][j] = m[i,:].dot(m[:,j])
    return p

def mul_submatrix(m,n):
    p = np.array(m)
    k = len(n)
    print(np.shape(p))
    for i in range(0,np.shape(p)[0],k):
        for j in range(0,np.shape(p)[1],k):
            p[i:i+k,j:j+k] = p[i:i+k,j:j+k].dot(n)
    return p

def resize(m,a,b):
    r = len(m)
    c = len(m[0])
    p = np.array([[m[i%r][j%c] for j in range(b)] for i in range(a)])
    return p

exec(input().strip())
