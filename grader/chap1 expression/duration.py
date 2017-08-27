h1 = int(input())*3600
m1 = int(input())*60
s1 = int(input())
h2 = int(input())*3600
m2 = int(input())*60
s2 = int(input())
t1 = h1 + m1 + s1
t2 = h2 + m2 + s2
dt = t2 - t1
dh = dt // (60*60)
dm = (dt - dh*3600) // 60
ds = dt - (dh*3600) - (dm*60)
print(str(dh)+":"+str(dm)+":"+str(ds)) 
