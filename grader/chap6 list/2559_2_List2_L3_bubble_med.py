d = [int(e) for e in input().strip().split()]
n = len(d)# n คือจํานวนขอมูลในลิสต=
for k in range(n-1): # ทําซ้ํา n-1 ครั้ง
    for i in range(n-1): # i = 0,1,2,...,n-2
        if d[i] > d[i+1]: # ถาตัวซาย > ตัวขวา ใหสลับคา
            d[i],d[i+1] = d[i+1],d[i]
#med
if n%2 == 0:
    med = (d[n//2 - 1]+d[n//2])/2
else:
    med = d[n//2]
print(float(med))
