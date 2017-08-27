n = "0123456789"
low = "abcdefghijklmnopqrstuvwxyz"
high = low.upper()
nl = [0]*10
high_l = [0]*len(high)
low_l = [0]*len(low)
s = input().strip()
for c in s:
    if c in n:
        nl[int(c)] += 1
    elif c in high:
        high_l[high.find(c)] += 1
    elif c in low:
        low_l[low.find(c)] += 1
print(" ".join(map(str,nl+high_l+low_l)))


        
