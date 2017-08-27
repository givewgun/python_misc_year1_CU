b = int(input().strip())
start,stop,step = [str(e) for e in input().strip().split()]
ol = [start,stop,step]
#-----change to base ten
# 101001 base 2 to ten (2^0)*1 +2^1()
nl = []
for c in ol:
    new = c[::-1]
    sum = 0
    for i in range(len(new)):
        sum += b**(i) * int(new[i])
    nl.append(sum)
#nl = list taht has been change to base ten
#new 10 base start stop step
start,stop,step = [int(e) for e in nl]
for i in range(start,stop,step):
    num = i
    if i == 0:
        print("0")
    else:
        bn = ""
        while num>0:
            r = num % b
            bn = str(r) + bn
            num = num // b
        print(bn)

    
    
