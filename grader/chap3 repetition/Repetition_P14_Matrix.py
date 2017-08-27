m,t = [int(e) for e in input().split()]
if t == 1:
    for i in range(1,m+1):
        for j in range(i,m+1): # 11 12 13 14 22 23 24 33 34 44
            print("("+str(i)+","+str(j)+")") 
elif t == 2:
    for i in range(1,m+1):
        for j in range(1,i+1):
            print("("+str(i)+","+str(j)+")") #44 43 42 41 33 32 31 22 21 11

elif t == 3:
    for i in range(1,m+1):#15 24 33 42 51 66 ...
        print("("+str(i)+","+str(m+1-i)+")") #i+j(ตน.แถว+ตน.หลัก) = m+1 (มิติ)
