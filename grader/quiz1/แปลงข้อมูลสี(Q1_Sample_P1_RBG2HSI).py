import math
r = float(input())
g = float(input())
b = float(input())
k = ((r-g) + (r-b)) / (2 * math.sqrt( (r-g)**2 + (r-b)*(g-b)))

h = 2*math.pi - math.acos(k)
s = 1 - (3*r)/(r+g+b)
i = (r+g+b)/3
print(h)
print(s)
print(i)
