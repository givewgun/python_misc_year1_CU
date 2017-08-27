un = [int(e) for e in input().strip().split()]
sort = []
while len(un) > 0:
    sort.append(min(un))
    un.remove(min(un))
print(sort)
