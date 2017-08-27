num = int(input().strip())
pos = []
while num >= 0:
    pos.append(num)
    num = int(input())
neg = []
neg.append(num)
for i in pos:
    print(i+neg[0])

    
