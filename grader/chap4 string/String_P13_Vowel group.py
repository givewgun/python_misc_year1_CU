s= input().strip()
v = "aeiou"
s2 = ""
for c in s:
    if c not in v:
        s2+= " "
    else:
        s2+= c
print(len(s2.split())) # count data/element in list
    
