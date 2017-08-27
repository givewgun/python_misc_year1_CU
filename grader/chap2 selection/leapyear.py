#leap year
year_be = int(input())
year_ce = year_be - 543
if (year_ce%4==0 and year_ce%100 !=0) or year_ce%400==0:print(29)
else:print(28)
