l = [e for e in input().strip().split()]
swap = [int(e) for e in input().strip().split()]
nl = []
for i in range(len(swap)):
    nl.append(l[swap[i]])
print(" ".join(nl).strip())
