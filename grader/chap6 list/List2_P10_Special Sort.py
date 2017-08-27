num = [int(e) for e in input().strip().split()]
even = []
odd = []
for i in num:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)
even = sorted(even)
odd = sorted(odd, reverse = True)
print(" ".join(map(str,even+odd)).strip())
