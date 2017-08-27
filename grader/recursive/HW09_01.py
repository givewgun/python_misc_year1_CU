fdic = dict()
def f(d,c,s,b,m):
    if (c,s,b,m) in fdic:
        return fdic[(c,s,b,m)]
    if s==len(d)-1:
        return m
    if b==True and d[s+1]>=d[s]:
        fdic[(c,s,b,m)] = f(d,c+1,s+1,True,max(c+1,m))
        return fdic[(c,s,b,m)]
    if b==True and d[s+1]<d[s]:
        fdic[(c,s,b,m)] = f(d,0,s+1,False,m)
        return fdic[(c,s,b,m)]
    if b==False and d[s+1]>=d[s]:
        fdic[(c,s,b,m)] = f(d,1,s+1,True,m)
        return fdic[(c,s,b,m)]
    fdic[(c,s,b,m)] = f(d,0,s+1,False,m)
    return fdic[(c,s,b,m)]

d = [int(x) for x in input().split()]
print(f(d,0,0,False,0)+1)
