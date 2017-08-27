#triangle side rule
a,b,c = [int(i) for i in input().split()]
if a+b>c and a+c>b and b+c>a: print('YES')
else: print('NO')
