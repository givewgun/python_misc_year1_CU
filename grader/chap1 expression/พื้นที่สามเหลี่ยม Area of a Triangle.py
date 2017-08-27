import math
a,b,c = [ int(e) for e in input().split()]
p = (a+b+c)/2
print(math.sqrt(p * (p-a) * (p-b) * (p-c)))
