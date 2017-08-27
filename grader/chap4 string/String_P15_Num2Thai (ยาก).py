n = input().strip().replace(",","")
unit = ['','sip','roey','pun','muen','saen','larn','sip','roey','pun','muen','saen','larn']
digit = ['soon','nueng','song','sam','see','ha','hok','jed','pad','kao']
s = ""
sd = ""
negative = False
if n[0] == '-':
    negative = True
#เดี๋ยวเติมลบตอนสุดท้าด้วย
    n = n[1:]
if '.' in n:
    sd = sd + "jood" + "-"
    d = n[n.find(".")+1:]
    n = n[:n.find(".")]
    for char in d:
        sd = sd + digit[int(char)] +"-"

    
#คิดหน้าทศนิยม---------------------

for i in range(len(n)): #i คือเลขยกกำลังของ10ที่จะมาหารดูหลัก เช่น หลักร้อบ 10**2
    index = int(n) // (10**i) %10 
    if i == 0:
        if len(n) == 1:
            s = s + digit[int(n)] + "-"
        elif len(n) > 1:
            if int(n)%10 == 1:
                s = s + "ed" + "-"
            elif int(n)%10 != 0:
                s = s + digit[int(n)%10] + "-"
    elif i == 1:
        if index == 1:
            s = unit[1] + "-" + s
        elif index == 2:
            s = "yee" + "-" + unit[1] + "-" + s
        elif index != 0: #103 หนึ่ง ร้อย สาม
            s = digit[index] + "-" + unit[1] + "-" + s
    elif i == 6 and len(n)>7 and index == 1: #9,991,000,000
        s = "ed" + "-" + unit[i] + "-" + s
    elif i == 7:#หลักสิบล้าน
        if index == 1:
            s = unit[1] + "-" + s
        elif index == 2:
            s = "yee" + "-" + unit[1] + "-" + s
        elif index != 0: #103 หนึ่ง ร้อย สาม
            s = digit[index] + "-" + unit[1] + "-" + s     
    else:
        if index != 0:
            s = digit[index] + "-" + unit[i] + "-" + s
if len(n) > 7 and "larn" not in s:
    s = s + "larn" + "-"
#อย่าลืมใส่ลบ
if negative == True:
    print("lop" + "-" + (s+sd)[:-1])
else:
    print((s+sd)[:-1])
    
