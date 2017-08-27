data = [int(e) for e in input().strip().split() ]
avg = ""
if len(data) == 1:
    avg += str(data[0])
else:
    for i in range(len(data)):
        if i == 0:
            avg += str( (data[i]+data[i+1])//2 ) + " "
        elif i == len(data)-1:
            avg += str( (data[i]+data[i-1])//2 ) + " "
        else:
            avg += str( (data[i-1]+data[i]+data[i+1])//3 ) + " "
print(avg.strip())
