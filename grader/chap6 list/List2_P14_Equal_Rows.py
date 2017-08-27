row = int(input().strip())
col = int(input().strip())
m = []
for t in range(row):
    m.append(input().strip().split())
for i in range(row):
    for j in range(i+1,row):
        if m[i] == m[j]:
            print(i+1)#because when use range, we use the index not the real row pos
            print(" ".join(m[i]))
            print(j+1)
            print(" ".join(m[i]))


    
        
