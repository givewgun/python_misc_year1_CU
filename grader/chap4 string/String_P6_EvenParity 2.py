n = input()
count1 = 0
for char in n:
    if char == "1":
        count1 += 1
if count1 % 2 == 0:
    print(n + "0")
else:
    print(n + "1")
