n = int(input())
ans = ""
for i in range(n-1,1,-1):#ไล่จากมากไปน้อย
    if n % i == 0:
        ans += str(i) + " "
if len(ans) == 0:
    print('Prime Number')
else:
    print(ans)
