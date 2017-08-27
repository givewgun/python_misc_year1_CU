a = [int(e) for e in input().strip()[1:-1].split(",")]
b = [int(e) for e in input().strip()[1:-1].split(",")]
sum = 0
for i in range(len(a)):
    sum += a[i] * b[i]
print(sum)
