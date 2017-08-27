infile = open(input().strip(),'r')
be = 0
se = 0
ve = 0
et = 0
for line in infile:
    d = line.strip().lower().split()
    if d[0] == 'be':
        be += 1
    elif d[0] == 'se':
        se += 1
    elif d[0] == 've':
        ve += 1
    elif d[0] == 'et':
        et += 1
print(be,se,ve,et,be+se+ve+et)
