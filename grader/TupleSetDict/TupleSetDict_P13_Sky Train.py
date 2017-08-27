station = dict()
while True:
    data = input().strip().split()
    if len(data) == 1:
        search = data[0]
        break
    else:
        for d in data:
            if d not in station:
                station[d] = set(data)
            else:
                station[d].update(set(data))
#แนวคิดคือการใช้set ละเราก็เอาค่่าvalueที่เราเก็บไว้ตอนแรก มาใช้เป็นkeyเพื่อหาสถานีต่อจากมันอีกๅ อีกที
#ละคือมันเป็นset ดังนั้นไม่ต้องกลัวว่าจะซ้ำเลย

if search not in station:
    print(search)
else:
    out = set()
    for c in station[search]:
        out.update(set(station[c]))
    out = sorted(out)
    for c in out:
        print(c)
