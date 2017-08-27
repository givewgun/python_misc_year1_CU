x = int(input())
s = 0
while x>=0:
    if x % 2 == 0:
        s += x
        x = int(input())
    else:
        x = int(input())
print(s)
