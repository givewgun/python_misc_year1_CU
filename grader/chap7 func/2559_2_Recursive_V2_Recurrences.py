def h(n): # Tower of Hanoi
    if n == 0:
        return 0
    elif n >= 1:
        return 2*h(n-1)+ 1
def gcd(x,y): # Greatest Common Divisor
    if y == 0:
        return x
    elif y > 0:
        return gcd(y,x%y)
def J(n,k): # Josephus Problem
    if n == 1:
        return 0
    elif n >1:
        return (J(n-1,k)+k) % n
def C(n): # Catalan Number
    s = 0
    if n == 0:#C(0) C(n+1) :C(2) = C(0)C(1) + C(1)C(0)
        return 1
    elif n >= 1:
        for k in range(n):
            s += C(k)*C(n-1-k)
        return s

def f(n): # Fibonacci Number
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 1 and n%2 == 0:
        k = int((n)/2)
        return (2*f(k-1)+f(k))*f(k)
    elif n >= 2 and n%2 != 0:
        k = int((n+1)/2)
        return f(k)*f(k) + f(k-1)*f(k-1)

def F(n): # Female sequence
    if n == 0:
        return 1
    elif n>0:
        return n - M(F(n-1))
def M(n): # Male sequence
    if n == 0:
        return 0
    elif n>0:
        return n - F(M(n-1))
    
def A(m,n): # Ackermann Number'''
    if m == 0:
        return n+1
    elif m>0 and n == 0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))
    
exec(input().strip()) # do not remove this line
