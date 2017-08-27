#fibbonacci


def f(n):   #Slow
    if n==0 :
        return 0
    if n==1 :
        return 1
    return f(n-1) + f(n-2)



def f2(n): #Fast
    F = [0]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
    
n = int(input('n = '))
print(f2(n))
print(f(n))

