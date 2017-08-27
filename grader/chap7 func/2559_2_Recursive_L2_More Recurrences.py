def x(n): # Logistic Map
    if n == 0:
        return 0.01
    elif n>0:
        k = x(n-1)
        return 3 * k * (1-k)
def M(n): # Motzkin number
    sum = 0
    if n == 0 or n == 1:
        sum += 1
    elif n >= 2:
        for k in range(n-1):
            sum += M(k)*M(n-2-k)
        sum += M(n-1)
    return sum
def D(m,n): # Delannoy number
    if n == 0 or m == 0:
        return 1
    return D(m-1,n) + D(m-1,n-1) + D(m,n-1)
def S(n): # Schroder-Hipparchus number
    if n == 1 or n ==2:
        return 1
    elif n>= 3:
        return int((1/n) * ((6*n-9)*S(n-1) - (n-3)*S(n-2)))
def d(n): # Number of Derangements
    if n == 0:
        return 1
    elif n>= 1:
        return n*d(n-1) + (-1)**n
exec(input().strip()) # do not remove this line

