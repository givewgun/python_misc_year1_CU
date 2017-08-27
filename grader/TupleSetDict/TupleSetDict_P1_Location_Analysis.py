num = int(input().strip())
user = list()
user_d = dict()
for i in range(num):
    data = input().strip()
    colon = data.find(":")
    id = data[:colon]
    city = { e for e in data[colon+1:] if e not in ", 0123456789"}
    user.append([id,city])
    user_d[id] = city

id = input().strip()
out = []
found = False
for i in user:
    if i[0] != id and i[1].intersection(user_d[id]) != set() :
        out.append(i[0])
        found = True
        
if not found:
    print("Not Found")
else:
    for c in out:
        print(c)

