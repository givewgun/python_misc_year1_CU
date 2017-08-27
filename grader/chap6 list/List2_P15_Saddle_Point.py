row,col = [int(e) for e in input().strip().split()]
m = []
for t in range(row):
    m.append([int(e) for e in input().strip().split()])
#-----------
saddle = False
i = 0
while i<row and saddle == False:
    for j in range(col):
        x = m[i][j]
        r = m[i]
        co = []
        for c in m:
            co.append(c[j])
        if x == min(r) and x == max(co):
            print(x)
            saddle = True
            break
    i += 1
        
if saddle == False:
    print(-1)

        
