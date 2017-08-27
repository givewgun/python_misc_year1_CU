s = input().strip()
c1 = input().strip()
c2 = input().strip()
new = ""
for char in s:
    if  char in c1:
        new += c2[c1.index(char)] # string.index("char") will return the index of that char in that string
    elif char in c2:
        new += c1[c2.index(char)]
    else:
        new += char
print(new)
