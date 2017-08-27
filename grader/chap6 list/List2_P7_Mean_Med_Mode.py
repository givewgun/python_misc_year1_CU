t =int(input().strip())
l = []
for i in range(t):
    l.append(int(input().strip()))
l = sorted(l)
#Mean
mean = sum(l)/len(l)
#med
if len(l)%2 == 0:
    med = (l[len(l)//2 - 1]+l[len(l)//2])/2
else:
    med = l[len(l)//2]
#mode
no_recur = []
max = 0
for c in l:
    if c not in no_recur:
        no_recur.append(c)
for c in no_recur:
    if l.count(c) >= max:
        mode = c
        max = l.count(c)
    
print(mean,med,mode)
