#Babylonian method of finding square root
'''
a = float(input('a = ')) Shitty prog
x0 = 1            or   x = 1
x1 = (x0+a/x0)/2       x = (x+a/x)/2
x2 = (x1+a/x1)/2       x = (x+a/x)/2
x3 = (x2+a/x2)/2            ...
x4 = (x3+a/x3)/2
x5 = (x4+a/x4)/2
x6 = (x5+a/x5)/2
print(x6, a**0.5)
'''

a = float(input('a = '))
x = 1
while abs(x**2 - a) > 1e-10 : #absดีกว่า เพราะfloat มันเป็นค่าประมาณ เอาที่ยอมรับได้ดีกว่า
   x = (x+a/x)/2 #float เก็บค่าประมาณนะ บางทีมัน!= ตั้งต้น
print(x, a**0.5)
