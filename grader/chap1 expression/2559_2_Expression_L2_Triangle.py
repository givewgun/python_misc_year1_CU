import math
#sin cos etc(angle) in radians
a = float(input()); b = float(input()); C = float(input())
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))
print("c =",c,"cm.")
