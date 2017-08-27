#rotate 13 แทนตัวอักษรด้วยตัวอักษรที่ถัดไปอีก13ตัว 
#(13+1 คือตัวที่14เริ่มนับจากมันนั่นเอง(นับตัวเองเป็น1)
#ใช้indexในการทำนะ
#อันนี้แบบใช้file txt เลย
'''
           1         2          3             4         5     
 01234567890123456789012345 6789012345678||||9012345678901
"ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLM||||NOPQRSTUVWXYZ"
  ^            ^(1+13)
'''
filename = input('Enter file name ; ' )
infile = open(filename , 'r')
outfile = open(filename + '.rot13', 'w')#ไฟล์เพื่อบันทึกที่แปลงแล้ว
for line in infile:
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = upper.lower() #lower สองที่ในบรรทัดนี้มีต.หมายต่างกัน
    rot13 = ''
    for c in line: #แปลงเป็นlineๆเลย
        if c in upper:
            rot13 += upper[(upper.find(c)+13) % 26] #เพราะว่าเพ่มทีละ13และตัวที่13+13คือ26ก็คือเริ่มใหม่(1)เลย 
        elif c in lower:                            #เช่นrot13 n คือตัวที่13+13 %26 คือindex0 คือ a นั่นเอง
            rot13 += lower[(lower.find(c)+13) % 26]
        else:
            rot13 += c
    outfile.write(rot13)

infile.close()
outfile.close()
