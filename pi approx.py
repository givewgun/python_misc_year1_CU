#PI APPROX
import math

n = 22
d = 7
pi = math.pi

while abs(pi-n/d) >= 1e-9 :
    delN = abs(pi - (n+1)/d)
    delD = abs(pi - n/(d+1))
    if delN < delD :
        n = n + 1
    else:
        d = d + 1

print(n, '/',d,'=',n/d)
