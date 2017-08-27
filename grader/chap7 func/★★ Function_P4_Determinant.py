def det3(m):
# รับ input m ในรูปแบบ [[1,2,3],[4,5,6],[7,8,9]]
    a = m[0][0]*m[1][1]*m[2][2]
    b = m[0][1]*m[1][2]*m[2][0]
    c = m[0][2]*m[1][0]*m[2][1]
    d = m[0][2]*m[1][1]*m[2][0]
    e = m[0][0]*m[1][2]*m[2][1]
    f = m[0][1]*m[1][0]*m[2][2]
    return a+b+c-d-e-f
def det4(m):
    # ให้เขียน function เองที่นี่
    #เวลาตัด คือ มันตัวrow1 และแถวไล่จาก 0 1 2 3 (ดูรูปประกอบ)
    #[[a,b,c,d],[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sum = 0
    for i in range(4):
        nm = []
        for r in m[1:]:#ตัดrow1
            nr = r[:]#ตัวcopy
            nr.pop(i)
            nm.append(nr)
        #print(nm)
        sum += (-1)**i * m[0][i] * det3(nm)
    return sum
matrix = []
for i in range(4):
    matrix.append([int(e) for e in input().split()])
print(det4(matrix))
