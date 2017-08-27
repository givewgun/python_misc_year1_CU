dat = [ int(e) for e in input().strip().split()]
count = 0
sum = 0
for i in dat:
    if i < 0:
        break
    else:
        sum += i
        count += 1
    
print(sum/count)
