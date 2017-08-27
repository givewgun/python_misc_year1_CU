n = int(input().strip())
user2page = {}
page2user = {}
for i in range(n):
    x = input().strip().split()#Sukree Food Panda Movie

     # เพิ่ม set ของ page ลงใน user2page
    if x[0] in user2page.keys():
        user2page[x[0]].update(x[1:])
    else:
        user2page[x[0]] = set(x[1:])          
 # เพิ่ม set ของ user ลงใน page2user
    for j in x[1:]:#Sukree Food Panda Movie
        if j in page2user.keys():
            page2user[j].add(x[0])
        else:
            page2user[j] = {x[0]}

while True:
    x = input().strip().split()
    if len(x) == 1: break
    elif x[0] == 'common' and x[1] == 'page':#common page Somchai Sukree
        if x[2] not in user2page.keys(): # สร้าง set เริ่มต้นในการหาตัวร่วม
            ans = set()
        else:
            ans = user2page[x[2]]
        for i in x[3:]: # น าแต่ละ set ในค าถามมาหาตัวร่วม
            if i not in user2page.keys():
                ans = ans.intersection({})
            else:
                ans = ans.intersection(user2page[i])
        print(len(ans))
    elif x[0] == 'common' and x[1] == 'user':#common user Panda Food
        if x[2] not in page2user.keys(): # สร้าง set เริ่มต้นในการหาตัวร่วม
            ans = set()
        else:
            ans = page2user[x[2]]
        for i in x[3:]: # น าแต่ละ set ในค าถามมาหาตัวร่วม
            if i not in page2user.keys():
                ans = ans.intersection({})
            else:
                ans = ans.intersection(page2user[i])
        print(len(ans)) 
    elif x[0] == 'similar' and x[1] == 'user':#similar user Somchai

        if x[2] not in user2page.keys(): # สร้าง set ของเพจที่กดไลก์โดยคนที่อยู่ในค าถาม
            pageset = set()
        else:
            pageset = user2page[x[2]]
        maxuser = list(user2page.keys())[0] # ใส่ค่าตั ้งต้น ให้เป็นคนแรกที่อยู่ใน user2page
        if maxuser == x[2]: # เผื่อว่าชื่อตรงกับช่อง 0 ให้ไปเลือกช่องที่ 1 แทน
            maxuser = list(user2page.keys())[1]
        # คิดค่าความเหมือนระหว่าง pageset กับเพจที่ maxuser กดไลก์
        maxvalue = len(pageset.intersection(user2page[maxuser])) / len(pageset.union(user2page[maxuser]))

        for i in user2page.keys(): # ไล่เปรียบเทียบกับทุก user
            # คิดค่าความเหมือนระหว่าง pageset กับเพจที่ i กดไลก์
            value = len(pageset.intersection(user2page[i])) / len(pageset.union(user2page[i]))
            if i != x[2] and (value > maxvalue or \
                              (value == maxvalue and i < maxuser)):
                maxvalue = value # ตั ้งค่า max ใหม่
                maxuser = i
        print(maxuser)
    elif x[0] == 'similar' and x[1] == 'page':#similar page MaewMeow
        if x[2] not in page2user.keys(): # สร้าง set ของคนที่กดไลก์โดยคนที่อยู่ในค าถาม
            userset = set()
        else:
            userset = page2user[x[2]]
        maxpage = list(page2user.keys())[0] # ใส่ค่าตั ้งต้น ให้เป็นเพจแรกที่อยู่ใน page2user
        if maxpage == x[2]: # เผื่อว่าเพจตรงกับช่อง 0 ให้ไปเลือกช่องที่ 1 แทน
            maxpage = list(page2user.keys())[1]
        # คิดค่าความเหมือนระหว่าง userset กับuserที่กดไลก์เพจ
        maxvalue = len(userset.intersection(page2user[maxpage])) / len(userset.union(page2user[maxpage]))

        for i in page2user.keys(): # ไล่เปรียบเทียบกับทุก เพจ
            # คิดค่าความเหมือนระหว่าง user กับuser ทีกดไลก์เพจ i
            value = len(userset.intersection(page2user[i])) / len(userset.union(page2user[i]))
            if i != x[2] and (value > maxvalue or \
                              (value == maxvalue and i < maxpage)):
                maxvalue = value # ตั ้งค่า max ใหม่
                maxpage = i
        print(maxpage)
