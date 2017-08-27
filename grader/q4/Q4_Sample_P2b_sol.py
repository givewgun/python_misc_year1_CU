def F(n):
    if n==0: return 0
    if n==1: return 1
    if n==2: return 1
    k=n//3
    if n%3==0:
        return 5*F(k)**3+3*(-1)**k*F(k)
    if n%3==1:
        return F(k+1)**3+3*F(k+1)*F(k)**2-F(k)**3
    if n%3==2:
        return F(k+1)**3+3*F(k+1)**2*F(k)+F(k)**3

def x(m,n):
    if m==0 or n==0: return m+n
    return x(m,n-1)+x(m-1,n)

def p(n):
    if n<=1: return n
    if n%2==0:
        return n+2*p(n-1)+p(n-2)
    return n+p(n-1)+2*p(n-2)

def z1(n):
    if n<10: return z2(n)
    return z1(z2(n))+z2(n)

def z2(n):
    if n<10: return n
    return n%10+z2(n//10)

exec(input().strip())  # do not remove this line