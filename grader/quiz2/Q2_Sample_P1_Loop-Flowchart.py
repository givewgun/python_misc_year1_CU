m = int(input().strip())
count = 0
num_perfects = 0
while count < m:
    n = int(input().strip())
    t = 0
    d = 1
    while d <= n/2:
        k = n%d
        if k == 0:
            t = t+d
        d += 1
    if t == n:
        s = str(n) + " is perfect"
        print(s)
        num_perfects += 1
        t = 0
        d = 1
        s = ""
        while d <= n/2:
            k = n%d
            if k == 0:
                t = t+d
                s += str(d) + ","
            d += 1
        print(s)
    else:
        s = str(n) + " is not perfect"
        print(s)
    count +=1
print(num_perfects)
