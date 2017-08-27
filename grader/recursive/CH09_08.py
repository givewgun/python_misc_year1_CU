trm = dict()
def warp(i,b):
    if i==b:
        return True
    if i not in trm:
        return False
    for k in trm[i]:
        if(warp(k,b))==True:
            return True
    return False

r,a,b = [int(x) for x in input().split()]
for i in range(r):
    c,d = [int(x) for x in input().split()]
    if c not in trm:
        trm[c] = list()
    trm[c].append(d)
ret = warp(a,b)
if ret==True:
    print("yes")
else:
    print("no")
