l = [int(e) for e in input().strip().split(", ")]
count = 0
for i in range(len(l)-1):
    if l[i] <0 and l[i+1] >= 0:
        count += 1
print(count)
