import numpy as np
def A(n,k):
    if n == 0:
        return np.identity(2, dtype = int) % k
    elif n == 1:
        return np.array([[0,1],[1,1]]) % k
    else:
        m = A(n//2,k)
        A_power = m.dot(m) % k
        if n%2 == 0:
            return A_power
        else:
            return A(1,k).dot(A_power)
def fib(n, k):
    return A(n,k)[0][1]
n,k = [int(e) for e in input().split()]
print( fib(n,k) )
