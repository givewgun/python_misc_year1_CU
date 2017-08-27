import numpy as np

def H(n):
    if n==1:
        return np.array([[1]])
    h = H(n-1)
    l = h.shape[0]
    r = np.zeros((2*l,2*l),int)
    
    r[0:l,0:l] = h
    r[0:l,l:2*l] = h
    r[l:2*l,0:l] = h
    r[l:2*l,l:2*l] = -h
    return r

def P(n):
    if n==1: return 1
    return 3*P(n-1)+M(n-1)

def M(n):
    if n==1: return 0
    return 3*M(n-1)+P(n-1)

def S(n):
    return P(n)-M(n)
    
exec(input().strip()) # do not remove this line
