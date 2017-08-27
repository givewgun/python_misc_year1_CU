t = int(input().strip())
l = []
for i in range(t):
    l.append(int(input().strip()))
l = sorted(l,reverse = True)
for i in l:
    print(i)
    
