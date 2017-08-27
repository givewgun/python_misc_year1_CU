#real day sun etc
#input date month year
d,m,y =[int(i) for i in input().split()]
if m<3:
    m+=12
    y-=1
# floor == หารปัดเศษ //
c = y//100; k = y%100
w = (d+ (26*(m+1)//10) + k + (k//4) + (c//4) +(5*c))%7
if w == 0:
    print('SAT')
elif w == 1:
    print('SUN')
elif w == 2:
    print("MON")
elif w == 3:
    print("TUE")
elif w == 4:
    print("WED")
elif w == 5:
    print("THU")
elif w== 6:
    print("FRI")
