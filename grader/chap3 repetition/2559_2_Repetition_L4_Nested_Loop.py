n = int(input())
s = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        for k in range(j,0,-1):
            s += ((-1)**i ) * j * k
print(s)
