fdic = {0:0,1:1}
def fibo(k):
    if k in fdic:
        return fdic[k]
    if k==0 or k==1:
        return k
    ans = fibo(k-1)+fibo(k-2)
    fdic[k]=ans
    return ans
print(fibo(int(input())))
