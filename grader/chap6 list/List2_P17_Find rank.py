
data = dict()
while True:
    s = [float(e) for e in input().strip().split()]
    if len(s) == 1:
        find = s[0]
        break
    else:
        if s[1] not in data:
            data[s[1]] = [s[0]]
        else:
            data[s[1]].append(s[0])
score = sorted(data.keys(),reverse = True)
out = []
for s in score:
    out.extend(sorted(data[s]))
if find in out:
    print(out.index(find) + 1)
else:
    print("Not Found")

