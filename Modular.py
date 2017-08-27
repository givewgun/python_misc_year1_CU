#Moduluar exponential
def power_mod(a,k,m):
    if k == 0 : #base case
        return 1
    p = power_mod(a,k//2,m) * power_mod(a,k//2,m)
    if (k % 2) == 1:
        p *= a #k is odd
    return p % m

print(power_mod(2,100,10))
