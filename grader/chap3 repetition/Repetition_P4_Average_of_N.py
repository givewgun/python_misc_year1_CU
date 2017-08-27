data = int(input())
sum = 0
if data == 0:
    print("No Data")
else:
    for i in range(data):
        sum += float(input())
    print(sum/data)
