f = open(input().strip())
c_sum = 0
for line in f:
 for c in line : # เครื่องหมายเว้นวรรคและขึ ้นบรรทัดใหม่ ถือเป็นข้อมูลนิสิตต้องน าไปค านวณรวมกับตัวอักษรอื่น ๆ ด้วย
     c_sum = c_sum ^ ord(c) # ord(c) ใช้เปลี่ยน c ให้เป็นรหัส Unicode และเครื่องหมาย ^ คือ การ Exclusive OR
f.close()
print(c_sum)