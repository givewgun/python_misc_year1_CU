t = int(input().strip())
l = []
for i in range(t):
    l.append(input().strip())
#---bubble-----
count = 0
while True:
    sorted = True
    for i in range(len(l)-1):
        if len(l[i]) > len(l[i+1]):
            l[i],l[i+1] = l[i+1],l[i]
            count += 1
            sorted = False
        elif len(l[i]) == len(l[i+1]) and l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            count += 1
            sorted = False
    if sorted == True:
        break
#-------
for c in l:
    print(c)
print(count)
