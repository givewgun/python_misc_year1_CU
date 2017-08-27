#Days of Month
month, year_be = [str(i) for i in input().split()]
year_ce = int(year_be) - 543
month_31 = ['1','3','5','7','8','10','12']
month_30 = ['4','6','9','11']
if month == '2':
    if (year_ce %4 ==0 and year_ce % 100 !=0) or year_ce%400==0:
        print(29)
    else:
        print(28)
elif month in month_31:
    print(31)
else:
    print(30)
