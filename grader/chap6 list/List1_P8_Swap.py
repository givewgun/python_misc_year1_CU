l = [e+1 for e in range(int(input().strip())) ]
swap = [int(e) for e in input().strip().split()]
while swap != [0,0]:
    i1 = l.index(swap[0])
    i2 = l.index(swap[1])
    l[i1],l[i2] = swap[1],swap[0]
    swap = [int(e) for e in input().strip().split()]
print(l)
