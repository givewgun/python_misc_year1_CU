n = int(input().strip())
event = dict()
#-------- all events
for i in range(n):
    data = list({e for e in input().strip().split()}) #setก่อน ลบตัวซ้ำ ละใช้list
    for d in data:#กำจัดที่ซ้ำในบรรทัดออกไปละ ไม่จำเป็นต้องใช้setอีกต่ลอดไป
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
    recur = dict() #recur กล่าวซ้ำกี่ครั้ง ตรงข้าม occur
    for e in data:
        if e not in recur:
            recur[e] = 1
        else:
            recur[e] += 1
    #--- สลับkey valueเป็นจนครั้งที่แนะนำกับeventที่มีจน.ครั้งนั้นๆ
    occur = dict()
    for key in recur:
        value = str(recur[key])
        if value not in occur:
            occur[value] = [key]
        else:
            occur[value].append(key)
    #sort จน.ครั้งมากไปน้อย
    s_occurence = sorted(occur.keys(),reverse = True)
    for i in s_occurence:
        for event in sorted(occur[i]): #sort ตามพจนานุกรม
            print(event, i )
            
    
