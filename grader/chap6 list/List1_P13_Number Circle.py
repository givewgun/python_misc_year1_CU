data_n = int(input().strip())
data = [""]
for i in range(data_n):
    data.append(input().strip())
new = ['1']
while len(new) < data_n:
    new.append(data[int(new[-1])])
print(" ".join(new).strip())


"""
for i in range(1,data_n+1):
    right = input().strip()
    data.append([str(i),right])
#-------------
new = [e for e in data[0]]
while len(new) < data_n:
    for d in data:
        if d[0] == new[-1]:
            new.append(d[1])
print(" ".join(new[:-1]).strip())

for d in data:
    if d[0] in new:
        index = new.index(d[0])
        new.insert(index+1,d[1])
    elif d[1] in new:
        index = new.index(d[1])
        new.insert(index,d[0]) #insert(that index will be before)
    else:
        new.extend(d)
s = ""
for i in new:
    if i not in s:
        s += i + " "
print(s.strip())
"""
