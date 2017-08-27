ksd = dict()
def KS(i,w,v,x):
    if (i,x) in ksd:
        return ksd[(i,x)]
    if i<0:
        return 0
    if x>=w[i]:
        a1 = KS(i-1,w,v,x)
        a2 = KS(i-1,w,v,x-w[i])+v[i]
        if a1>a2:
            ksd[(i,x)]=a1
            return a1
        else:
            ksd[(i,x)]=a2
            return a2
    if x<w[i]:
        ksd[(i,x)]=KS(i-1,w,v,x)
        return ksd[(i,x)]

w = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
W = int(input())
print(KS(len(w)-1,w,v,W))
