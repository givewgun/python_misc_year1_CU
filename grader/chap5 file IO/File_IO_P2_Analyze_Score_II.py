infile = open(input().strip(),'r')
l = 0
for line in infile:
    if l == 0:
        n = int(line.strip())
    elif 0<l<=n:
        d = line.strip().split()
        s = 0
        for i in d[1:]:
            s += int(i)
        if 80<=s<=100:print(d[0],'A')
        elif 75<=s<=79:print(d[0],'B+')
        elif 70<=s<=74:print(d[0],'B')
        elif 65<=s<=69:print(d[0],'C+')
        elif 60<=s<=64:print(d[0],'C')
        elif 55<=s<=59:print(d[0],'D+')
        elif 50<=s<=54:print(d[0],'D')
        elif s<50:print(d[0],'F')
    l += 1
