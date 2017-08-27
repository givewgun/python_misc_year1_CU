r,c = [ int(e) for e in input().strip().split()]
m1 = []
m2 = []
for n in range(r):
    data = [int(e) for e in input().strip().split()]
    m1.append(data)
for n in range(r):
    data = [int(e) for e in input().strip().split()]
    m2.append(data)

m3 = []
for i in range(r):
    data = []
    for j in range(c):
        data.append(m1[i][j] + m2[i][j])
    m3.append(data)

for row in m3:
    print(" ".join(map(str,row)).strip())

    
