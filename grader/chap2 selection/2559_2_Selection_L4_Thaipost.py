type = input().strip()
w = int(input())
if type == "E":
    if w<0 or w>1e5:
        print('ERROR')
    else:
        if w<=20:print(32) # w in grams
        elif 20<w<=100:print(37)
        elif 100<w<=250:print(42)
        elif 250<w<=500:print(52)
        elif 500<w<=1000:print(67)
        elif 1000<w<=1500:print(82)
        elif 1500<w<=2000:print(97)
        elif 2000<w<=2500:print(122)
        elif 2500<w<=3000:print(137)
        elif 3000<w<=3500:print(157)
        elif 3500<w<=4000:print(177)
        elif 4000<w<=4500:print(197)
        elif 4500<w<=5000:print(217)
        elif 5000<w<=5500:print(242)
        elif 5500<w<=6000:print(267)
        elif 6000<w<=6500:print(292)
        elif 6500<w<=7000:print(317)
        elif 7000<w<=7500:print(342)
        elif 7500<w<=8000:print(367)
        elif 8000<w<=8500:print(397)
        elif 8500<w<=9000:print(427)
        elif 9000<w<=9500:print(457)
        elif 9500<w<=10000:print(487)
elif type == "N": 
    if w<0:
        print('ERROR')
    else:
        if w<1000:print(20)
        elif 1000<w<=2000:print(35)
        elif 2000<w<=3000:print(50)
        elif 3000<w<=4000:print(65)
        elif 4000<w<=5000:print(80)
        elif 5000<w<=6000:print(95)
        elif 6000<w<=7000:print(110)
        elif 7000<w<=8000:print(125)
        elif 8000<w<=9000:print(140)
        elif 9000<w<=10000:print(155)
        elif 10000<w<=11000:print(170)
        elif w>11000:
            print(170 + 15*((w-11000)//1000))
elif type == "R":
    if w<0 or w>2000:
        print('ERROR')
    else:
        if w<100:print(18)
        elif 100<w<=250:print(22)
        elif 250<w<=500:print(28)
        elif 500<w<=1000:print(38)
        elif 1000<w<=2000:print(58)
            
        
            
        
            
        
