#DAy of year
date = int(input())
month = int(input())
year_ce = int(input())-543 #input is in BE
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
day = 0

for i in range(1,month):
    if i in month_31:
        day += 31
    elif i == 2:
        if  (year_ce%4==0 and year_ce%100 !=0) \
           or year_ce%400==0:
            day += 29
        else:
            day += 28
    elif i in month_30:
        day += 30
day += date
print(day)
    
    
    
    
