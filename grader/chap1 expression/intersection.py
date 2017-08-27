a1,b1,c1 = [ float(i) for i in input().split()]
a2,b2,c2 = [ float(i) for i in input().split()]
x = (c2*b1 - c1*b2) / (a1*b2 - a2*b1)
y = (c2*a1 - c1*a2) / (a2*b1 - a1*b2)
print("("+str(x)+","+str(y)+")")
