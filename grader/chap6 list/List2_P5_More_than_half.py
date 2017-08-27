l = []
no_recur = []
s = input().strip()
while s != "-1":
    l.append(s)
    s = input().strip()
max = len(l)/2
for c in l:
    if c not in no_recur:
        no_recur.append(c)
found = False
for c in no_recur:
    if l.count(c) > max:
        print(c)
        found = True
if found == False:
    print("Not found")
    
