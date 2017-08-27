'''จงเขียนโปรแกรมเพื่อรับเส้นตรง 2 เส้นดังสมการด้านล่าง จากนั้นค านวณว่า สมการดังกล่าวมีค าตอบ 1 ค าตอบ
(one solution), ไม่มีค าตอบ (no solution), หรือมีค าตอบมากกว่า 1 ค าตอบ (many solutions)
L1 : a1x+b1y+c1=0
L2 : a2x+b2x+c2 = 0

น่าจะต้องใช้matrix
x = [[a1 b1]
    [a2 b2]]   หา det ถ้า detx != 0 1so;
                         det x = 0 many sol or no sol(a1=a2 b1=b2 c1!=c2
'''
a1,b1,c1 = [ int(i) for i in input().split()]
a2,b2,c2 = [ int(i) for i in input().split()]
#slope = -b1 / a1 =  -b2/a2
det = (a1*b2)-(a2*b1)
if det != 0:
    print("one solution")
else:
    if a1==a2 and b1==b2 and c1== c2: # 111 111
        print("many solutions")
    elif a1== a2 == 0 and (b1!=0 and b2!= 0):#y=...
        if c1/b1 == c2/b2: #y=2,0 2y=4,0 guarantee no .../0
            print("many solutions")
        else:
            print("no solution")
    elif (a1!= 0 and a2==0) and b1==b2==0: #x=... (same as y=)
        if c1/a1 == c2/a2:
            print("many solutions")
        else:
            print("no solution")
    elif -b1/a1 == -b2/a2: #ตรวจดูว่าขนานไหม
        if c1==c2==0 or c1/c2 == a1/a2:#ดูว่ามันถูกคูณทั้งสมการไหม(same line) 123 246
            print("many solutions")
        else:
            print("no solution") #ขนานคู่กันไป
    else: print("no solution") #ไม่อยู่ในกรณีเชคละ(ตัวประหลาด)
