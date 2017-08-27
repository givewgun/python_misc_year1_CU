a,b,c = [ int(e) for e in input().split() ]
if a != 0 and (b%a == 0 or c%a != 0):
    d = b//a +c%a

else:
    d = int(input())
if d<b:
    b = b*2
    a,c = c,a
    if b>a+c:
        d = d + b//2
        c = c-1
if d<b and d%2 == 0:
    a = a+b-d
    c = c+1
elif d==b:
    a = a-1
elif d>a+c:
    b = b**2
else:
    d = d+b
print(a,b,c,d)
