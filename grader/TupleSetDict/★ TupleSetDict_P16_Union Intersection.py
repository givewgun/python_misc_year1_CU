n = int(input().strip())
union = set()
inter = set()
for i in range(n):
    s = set(input().strip().split())
    if i == 0:
        union = s
        inter = s
    else:
        union = union.union(s)
        inter = inter.intersection(s)
print(len(union))
print(len(inter))
        
