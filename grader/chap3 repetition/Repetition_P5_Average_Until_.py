data = float(input())
sum = 0
count = 0
while data != -1:
    count += 1
    sum += data
    data = float(input())
if count == 0:
    print("No Data")
else:
    print(sum/count)
