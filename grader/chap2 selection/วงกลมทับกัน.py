'''
เราสามารถตรวจสอบว่าวงกลมสองวงแตะกันหรือทับกันหรือไม่ ด้วยการหาว่า ระยะห่างระหว่างจุดศูนย์กลางวงกลมมีค่าน้อยกว่า
หรือเท่ากันความยาวรัศมีของวงกลมรวมกันหรือไม่ ถ้าระยะห่างระหว่างจุดศูนย์กลางวงกลมมีค่าเท่ากับความยาวรัศมีของวงกลม
รวมกันแสดงว่าวงกลมทับกัน แต่ถ้าระยะห่างระหว่างจุดศูนย์กลางวงกลมมีค่าน้อยกว่ารัศมีของวงกลมรวมกันแสดงว่าวงกลมซ้อน
กัน ถ้าไม่อยู่ในสองเงื่อนไขนี้ แสดงว่าวงกลมไม่แตะกันและไม่ทับกันด้วย
งานของคุณ
รับจ ำนวนจริง 6 จ านวน เป็นพิกัด x, y และรัศมีของวงกลมทั้งสองวง แล้วบอกว่า วงกลมแตะกัน ซ้อนกัน หรือไม่แตะกันและไม
'''
#
#แตะกันตอบ 1 sqrt( (x1-x2)^2 + (y1-y2)^2) == r1+r2
#ซ้อนตอบ 2 sqrt( (x1-x2)^2 + (y1-y2)^2) < r1+r2
# ไม่แตะและไม่ซ้อน 3
import math
x1,y1,r1, x2,y2,r2 = [ float(e) for e in input().split()]
distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
if distance == r1+r2:
    print(1)
elif distance < r1+r2:
    print(2)
else:
    print(3)
