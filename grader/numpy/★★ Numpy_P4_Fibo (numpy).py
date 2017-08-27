import numpy as np
def fib(n, k): #เอามุมขวาบน
    if n == 0: return 0
    m = np.array([[0,1],[1,1]])
    a = np.array([[0,1],[1,1]])
    for i in range(n-1):
        m = m.dot(a) % k
    return m[0][1]
n,k = [int(e) for e in input().split()]
print( fib(n,k) )
