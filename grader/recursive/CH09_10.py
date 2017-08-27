cons = set()
ans = set()
def miss(x,k):
    if x in cons:
        return
    if x == "": return
    #print(x,k,len(x))
    if k==len(x):
        ans.add(x)
        cons.add(x)
        return
    for i in range(k,len(x)):
        #print(x,"i=",i,k)
        if x[i]==x[i].upper():
            miss(x[:i]+x[i+1:],i)
            miss(x,i+1)
    cons.add(x)
    ans.add(x)
    return
x = input().strip()
miss(x,0)
ans = list(ans)
ans = sorted(ans)
#print(ans)
for i in ans:
    print(i.strip())
