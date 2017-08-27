#Leap year
y = int(input('y = '))
d = 28
if y%400==0 or (y%4 == 0 and y%100 != 0):
    d = 29
print(d)
