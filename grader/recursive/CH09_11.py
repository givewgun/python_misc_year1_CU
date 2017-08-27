cdic = dict()
def c(n,k):
    if (n,k) in cdic:
        return cdic[(n,k)]
    if k==0 or n==k:
        return 1
    if 0 < k < n:
        ans = c(n-1,k)+c(n-1,k-1)
        cdic[(n,k)]=ans
        return ans
    return 0

n = int(input())
k = int(input())
print(c(n,k))
