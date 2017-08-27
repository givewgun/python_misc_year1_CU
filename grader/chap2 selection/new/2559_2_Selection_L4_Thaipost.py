#optimize by using list
ch = input().strip()
n = int(input())
price = 0
E = [0,20,100,250,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
Ep = [32,37,42,52,67,82,97,122,137,157,177,197,217,242,267,292,317,342,367,397,427,457,487]
N = [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000]
Np = [20,35,50,65,80,95,110,125,140,155,170]
R = [0,100,250,500,1000,2000]
Rp = [18,22,28,38,58]
if n < 0 or (ch == 'E' and n >10000) or (ch =='R' and n>2000): #maxmimum price of EMS and Register
    print('ERROR')
else:
    i = 0
    if ch == 'E': ch1 = E; price = Ep #create new variable for specific list and specific price
    elif ch == 'N': ch1 = N; price = Np
    elif ch == 'R': ch1 = R; price = Rp
    if n<=11000:
        while i<len(ch1):
            if n in range(ch1[i],ch1[i+1]+1): #like an interval until reaching the end of a price list
                print(price[i]) #the price will be equal to the position of the lowest of that in terval
                break #break
            i += 1
    elif ch == 'N' and n>11000:#Ceiling price of kg (same as below)
        a = n - 11000
        if a%1000 != 0:
            s = a//1000*15
            print(170 + s + 15)
        else:
            s = a//1000*15
            print(170 + s )
        
'''
if(n<0):
    print("ERROR")
else:
    if(ch=='N'):
        if(n<=1000):
            print(20)
        elif(n>1000 and n<=2000):
            print(35)
        elif(n>2000 and n<=3000):
            print(50)
        elif(n>3000 and n<=4000):
            print(65)
        elif(n>4000 and n<=5000):
            print(80)
        elif(n>5000 and n<=6000):
            print(95)
        elif(n>6000 and n<=7000):
            print(110)
        elif(n>7000 and n<=8000):
            print(125)
        elif(n>8000 and n<=9000):
            print(140)
        elif(n>9000 and n<=10000):
            print(155)
        elif(n>10000 and n<=11000):
            print(170)
        else:
            a=n-11000
            if(a%1000!=0): #เกินแล้วไม่เป็นกิโลโดดๆ(13500)จะปัดเศษขึ้นเลย( ละ+ราคาเพิ่ม
                s=a//1000*15 #2500 -> 2*15
                print(170+s+15) # s+15 = 3000g(ที่ปัดขึ้น ัน่นเอง)
            else:
                s=a//1000*15
                print(170+s)               
    elif(ch=='E'):
        if(n>10000):
            print("ERROR")
        elif(n<=20):
            print(32)
        elif(n>20 and n<=100):
            print(37)
        elif(n>100 and n<=250):
            print(42)
        elif(n>250 and n<=500):
            print(52)
        elif(n>500 and n<=1000):
            print(67)
        elif(n>1000 and n<=1500):
            print(82)
        elif(n>1500 and n<=2000):
            print(97)
        elif(n>2000 and n<=2500):
            print(122)
        elif(n>2500 and n<=3000):
            print(137)
        elif(n>3000 and n<=3500):
            print(157)
        elif(n>3500 and n<=4000):
            print(177)
        elif(n>4000 and n<=4500):
            print(197)
        elif(n>4500 and n<=5000):
            print(217)
        elif(n>5000 and n<=5500):
            print(242)
        elif(n>5500 and n<=6000):
            print(267)
        elif(n>6000 and n<=6500):
            print(292)
        elif(n>6500 and n<=7000):
            print(317)
        elif(n>7000 and n<=7500):
            print(342)
        elif(n>7500 and n<=8000):
            print(367)
        elif(n>8000 and n<=8500):
            print(397)
        elif(n>8500 and n<=9000):
            print(427)
        elif(n>9000 and n<=9500):
            print(457)
        elif(n>9500 and n<=10000):
            print(487)
    elif(ch=='R'):
        if(n>2000):
            print("ERROR")
        elif(n<=100):
            print(18)
        elif(n>100 and n<=250):
            print(22)
        elif(n>250 and n<=500):
            print(28)
        elif(n>500 and n<=1000):
            print(38)
        elif(n>1000 and n<=2000):
            print(58)
'''
