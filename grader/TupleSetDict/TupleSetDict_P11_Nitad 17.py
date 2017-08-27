n = int(input().strip())
event = dict()
#-------- all events
for i in range(n):
    data = list({e for e in input().strip().split()}) #setก่อน ลบตัวซ้ำ ละใช้list
    for d in data:
        data_c = data[:]
        data_c.remove(d)
        if d not in event:
            event[d] = data_c
        else:
            event[d].extend(data_c)
#---------
search = input().strip()
if search not in event:
    print("Not Found")
    exit(0)
elif event[search] == []:
    print("No suggested event")
    exit(0)
else:
    data = event[search] #ได้listของกิจกรรมที่เสนอแนะด้วย
    recur = dict()
    for e in data:
        if e not in recur:
            recur[e] = 1
        else:
            recur[e] += 1
    most = max(recur.values())
    low_alpha = []
    for key in recur:
        if recur[key] == most:
            low_alpha.append(key)
    print(min(low_alpha) + "\n" + str(most))
    
