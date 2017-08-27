num = [ int(e) for e in input().strip().split()]
sum = int(input().strip())
pair = 0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == sum:
            pair += 1
print(pair)
