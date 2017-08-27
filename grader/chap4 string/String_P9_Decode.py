s = input().strip()
c1 = input().strip()
c2 = input().strip()
new = ""
for char in s:
    if char == c1:
        new += c2
    elif char == c2:
        new += c1
    else:
        new += char
print(new)
