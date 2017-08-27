#-------------------------------


#มีค่าa b c ที่ไม่กิน 15 อะไรบ้างที่ c^2 =a^2 + b^x
for a in range(1,15):
    for b in range(a,15): #ตัดตัวที่ซ้ำเช่น 3^2+4^2 and 4^2+3^2
        for c in range(b,15):
            if c**2 == a**2 + b**2:
                print(str(a)+'**2 +',\
                      str(b)+'**2 =',\
                      str(c)+'**2 +')

#new code
p = [ [x, y, z]\
              for x in range(1,15)\
              for y in range(x,15)\
              for z in range(y,15)\
              if x**2 + y**2 == z**2
    ]

print(' '.join(map(str , p)))
