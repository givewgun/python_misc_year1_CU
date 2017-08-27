length = int(input().strip())
dat = ['']*length
#----- main
for i in range(length):
    dat[i] = int(input())
#---interval
low,high = [int(e) for e in input().strip().split()]
print(sum(dat[low:high+1]))
