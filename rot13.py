#rotate 13 แทนตัวอักษรด้วยตัวอักษรที่ถัดไปอีก13ตัว 
#(13+1 คือตัวที่14เริ่มนับจากมันนั่นเอง(นับตัวเองเป็น1)
#ใช้indexในการทำนะ
'''
           1         2         3             4         5     
 012345678901234567890123456789012345678||||9012345678901
"ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM||||NOPQRSTUVWXYZ"
  ^            ^(1+13)
'''
line = input('Enter any text : ')
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower() #lower สองที่ในบรรทัดนี้มีต.หมายต่างกัน
upper2 = upper*2 #ภ้าจบที่M ใช้ upper2 = upper + upper[:13] ก็ได้
lower2 = lower*2 #ภ้าจบที่M ใช้ lower2 = lower + lower[:13] ก็ได้
rot13 = ''
for c in line:
    if c in upper:
        rot13 += upper2[upper.find(c)+13]
    elif c in lower:
        rot13 += lower2[lower.find(c)+13]
    else:
        rot13 += c
print('rot13 =', rot13)
