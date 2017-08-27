s = input()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for char in s:
    if char in upper:
        count += 1
print(count)
