#Is this an increasing-digit number? --->
''' Code แบบเลข ขวามาซ้าย
n = int(input('Number = ')) 
while n**2 ==0:
    print('It is zero you dumbass')
    n = int(input('Number = '))
is_increasing = True
right_of_d = 99
while n>0 :
    d = n % 10 #รอบแรก d คือหลักหน่วยของ n รอบสองคือหลักสิบ เทียบจากขวาไปซ้าย
    n //= 10
    if d >= right_of_d : #ตัวทางซ้ายไม่น้อยกว่าตัวทางขวา
        is_increasing =False
        break
    right_of_d = d
'''
#code แบบstring ชวาไปซ้าย
n = input('Enter digits : ')
is_increasing = True

while int(n)**2 ==0:
    print('It is zero you dumbass')
    n = input('Enter digits :')
    
prev_d = ''
for d in n:
    if d <= prev_d:
        is_increasing = False
        break
    prev_d = d

if is_increasing :
    print('Yes, this is an increasing-digit number')
else:
    print('No, this is not an increasing-digit number')
    
