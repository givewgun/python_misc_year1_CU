n = int(input())
count = 0
factor_num = 0
prime = ""
if n<0:
    print('input unavailable')
else:
    for i in range(2,n+1):
        factor_num = 0
        for j in range(2,i):
            if i%j == 0:factor_num += 1
        if factor_num == 0:
            prime += str(i) + " "
            count += 1
    if count == 0:
        print('none')
    else:
        print(prime)
