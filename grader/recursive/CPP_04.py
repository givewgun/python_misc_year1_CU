def gcd(x,y):
    if x>=y and x%y==0:
        return y
    else:
        return gcd(y,x%y)

a,b = [int(x) for x in input().split()]
print(gcd(a,b))
