import math
n,r,met = [ int(e) for e in input().split() ]
if met == 1:
  print(int(math.factorial(n)/math.factorial(n-r)))
elif met == 2:
  print(int(math.factorial(n)/math.factorial(n-r)/math.factorial(r)))
