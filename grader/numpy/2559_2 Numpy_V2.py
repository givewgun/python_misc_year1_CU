import numpy as np
x = [int(e) for e in input().strip().split()]
rentalrates = np.array(x)
#print(rentalrates)
sales = np.zeros((4,5),int)
for k in range(4):
    sales[k,:] = input().strip().split()
#print(sales)
totalsales = np.sum(sales,axis = 0)
#print(totalsales)
d = np.argmax(totalsales,)#ต ำแหน่งใน totalsales ที่มีค่ำมำกสุด [,,,,]
print(["Mon","Tue","Wed","Thu","Fri"][d],float(totalsales[d]))
#------
salesvalues = np.dot(rentalrates, sales)
for i in salesvalues:
    print(float(i),end = " ")
