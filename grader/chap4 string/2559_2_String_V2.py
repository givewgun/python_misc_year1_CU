s = input().strip()
o = ""
for c in s:
    if c == '"' or c == "'" or c == "," or c =="." or c == "(" or c == ")":
        o += " "
    else:
        o += c
print(o)
