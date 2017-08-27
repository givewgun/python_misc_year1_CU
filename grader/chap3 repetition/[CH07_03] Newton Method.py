a,b,c,x1,d = [ float(e) for e in input().split() ]
#f(x) = ax^2+bx+c
#f'(x) = 2ax+b
#x2 = x1 - (ax1^2+bx1+c)-2ax1b
xn = x1
xn_1 = x1 - (a*(x1**2) + b*(x1) + c)/(2*a*x1 + b)
n = 1
while abs(xn_1 - xn) > d: #ผลต่างใช้absoluteด้วย
    xn = xn_1 #อารมณ์ประมาณ xn=xn_2 ละใช้ xn_2-xn_1ต่อ...
    xn_1 = xn - (a*(xn**2) + b*(xn) + c)/(2*a*xn + b)
    n += 1 #บวกเพิ่ม1step
print(n)
