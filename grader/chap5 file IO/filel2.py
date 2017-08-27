f = open("data.txt", "r")
section = input().strip()
n = 0
sum = 0
for line in f:
    data = line.strip().split(":")
    if data[2] == (section):
        n += 1
        sum += float(data[3])
if n > 0:
    print(sum/n)
    exit(0)
else:
    print("Not Found")
    exit(0)