n = int(input())
r = 0
i = 0
while n>0:
    k = n%10
    r += k*(2**i)
    n //= 10
    i += 1
print(r)
