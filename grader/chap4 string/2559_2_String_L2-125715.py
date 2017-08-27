s = input().strip().lower()
c1 = 1
max = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c1 += 1
        if c1 > max:
            max = c1
    else:
        c1 = 1


print(max)
