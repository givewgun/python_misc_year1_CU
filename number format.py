#format number
number=(input('Enter your number '))
'''new = ''
# ab,cde,fgh,ijk,lmn len14
# 01 234 567 8910 111213
# ,ตน.ที่ n-3 , 14-3 : 11 8 5 2
for i in range(len(number)): #ใช้indexคิดแทน
    char = ''
    if i%3 == len(number)%3 and i != 0 : #ดูrelationจากด้านบน
        char = ','+number[i]
        new+= char
    else: new+= number[i]

print(new)
'''
#list.insert(index, obj)
num = list(number)
index_total = len(num)-1
for index in range(len(num)-3,0,-3): #len8 a b      c d e       f g h
    num.insert(index,',')       #             [8-3-3]     [8-3]
print("".join(num))
        
    
