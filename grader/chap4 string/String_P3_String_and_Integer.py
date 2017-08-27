s1,s2 = [ str(e) for e in input().split() ]
num = "0123456789"
count = 0
s1  = s1[0].upper() + (s1.lower())[1:] #s1[1:] แปลว่าเอาเริ่มที่ตัวที่1(index) จนจบ
for char in s2:
    if char in num:
        count += int(char)
print(s1,count)
