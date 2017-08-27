trm = dict()
def gopr(k):
    out = ""
    for i in range(len(k)):
        out+=str(k[i])
        if i!=len(k)-1:
            out+= " -> "
    print(out.strip())

    
def warp(i,b):
    #print(i,b)
    if i[-1]==b:
        gopr(i)
        return True
    if i[-1] not in trm:
        return False
    ret = False
    for k in trm[i[-1]]:
        tmp = list(i)
        tmp.append(k)
        #print(i,tmp,b,"going")
        if(warp(tmp,b))==True:
            ret = True
    return ret

r,a,b = [int(x) for x in input().split()]
for i in range(r):
    c,d = [int(x) for x in input().split()]
    if c not in trm:
        trm[c] = set()
    trm[c].add(d)
for c in trm:
    trm[c] = sorted(list(trm[c]))
ret = warp([a],b)
if  ret==False:
    print("no")
