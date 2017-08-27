import math
pdic = dict()
def pmod(a,k,m):
    if (a,k,m) in pdic:
        return pdic[(a,k,m)]
    if k==0:
        return 1
    if k%2==0:
        ans = (((a**math.floor(k/2))%m)**2)%m
        pdic[(a,k,m)] = ans
        return ans
    if k%2==1:
        ans = (a*((a**math.floor(k/2))%m)**2)%m
        pdic[(a,k,m)] = ans
        return ans
a,k,m = [int(x) for x in input().split()]
print(pmod(a,k,m))
