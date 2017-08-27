a = []
m = [int(e) for e in input().split()]
while len(m) != 0:
    a.append(m)
    m = [int(e) for e in input().split()]
else:
    b = [[j[i] for j in a] for i in range(len(a))] #in เป็นก้อนๆเลย
    for i in b:
        print(' '.join(map(str,i))) #map เปลี่ยนelementใน...เป็นtypeนั้น
