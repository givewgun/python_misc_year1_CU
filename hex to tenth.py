#แปลงฐาน16เป็นฐาน10
hex_in = input('Enter hex : ').strip().upper()
hex_digit = '0123456789ABCDEF'
decimal_out = 0
p = len(hex_in) - 1 # 16**3 16**2 16**1 16**0 ;n=4-(1)....

def MainBody(hex_in):
    global hex_digit
    global decimal_out
    global p
    for digit in hex_in:
        if digit in hex_digit :
            decimal_out += hex_digit.find(digit) * 16**p
            p -=1 #อย่าลืม ไม่งั้นค่าpมันจะเท่าเดิมตลอด
            #print(decimal_out)
 
    '''else:
        print('Invalid heximal number')
        exit(-1)'''

def Checker(hex_in): #check ว่าที่ใส่มามันhexไหม
    global hex_digit
    for digit in hex_in:
        if digit not in hex_digit : return False

def Method(hex_in):
    global hex_digit
    while True:
        while Checker(hex_in)==False: #ถ้าใส่มาไม่ใช่hex ลูปให้ไปใส่ใหม่->นำไปทำต่อ(ทับไปเลย)
            print('Invalid heximal number')
            hex_in = input('Enter hex : ').strip().upper()
        MainBody(hex_in)
        return decimal_out #อย่าลืมreturnผลลัพท์ที่ต้องการ
    

print('Final num = ',Method(hex_in))
