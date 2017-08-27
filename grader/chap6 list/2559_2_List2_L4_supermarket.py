file = open("inventory.txt","r")
data = []
for line in file:
    l = line.strip().split(";")
    if l != ['']:
        data.append(l[:2]+[int(l[2])])

all_id = [d[0] for d in data]#id ทั้งหมดที่ใส่มา
out = []
#-----
while True:#function คำสั่งอยู่ที่met[0] dataใดๆ [id,name,amount
    met = [e for e in input().strip().split()]
    if met[0] == "Q":
        out.append("Bye!")
        break
    else:
        id = met[1]
        if met[0] == "T": #ex T P400 -1000 หมายถึงใหเพิ่มจํานวนสินคารหัส P100 ไปอีก 200 รวมเป;น 1200
            if id not in all_id:#เช็คว่ามีของไหม
                out.append("Product code does not exist.")
            else:
                amount = int(met[2])
                index = all_id.index(id)
                data[index][2] += amount
                out.append(data[index][:])#**** see below
        elif met[0] == "U": #ex U P100 3000 หมายถึงใหเปลี่ยนจํานวนสินคารหัส P100 ใหเป;น 3000
            if id not in all_id:#เช็คว่ามีของไหม
                out.append("Product code does not exist.")
            else:
                amount = int(met[2])
                index = all_id.index(id)
                data[index][2] = amount
                out.append(data[index][:])
        elif met[0] == "A": #ex  A P300 Product-300 3000 หมายถึงใหเพิ่มรายการสินคาใหมเขาไปในลิสต โดย
            if id in all_id:#ของซ้ำ
                out.append("Duplicate product code.")
            else:
                data.append(met[1:3] + [int(met[3])]) #[0]มันคือฟังชั่น เราไม่เพิ่มในdataรวม
                all_id.append(met[1]) #เพิ่มidลงกองกลาง
                out.append(met[1:3] + [int(met[3])])
        elif met[0] == "D":#ลบ product D P100 
            if id not in all_id:#ไม่มีของให้ลบ  
                out.append("Product code does not exist.")
            else:
                index = all_id.index(id)
                data.pop(index)
                all_id.remove(met[1])#ลบidออกด้วย
                out.append(str(met[1])+ " deleted")
for c in out:
    print(c)

''' ****  
เวลาจะappendหรือเพิ่มค่าlistใดๆลงไปในตัวแปร/listอีกตัวที่เราต้องการให้มันเก็บค่านั้นๆ(instataneous record)
โดยจะไม่ไปยุ่งกับมันแน่นอนเราควรจะcpy list นั้นๆไว้เพื่อกันไม่ให้เปลี่ยนค่า
โดยทำยังงี้ list_new = list_เดิม[:] ([:]) เพื่อป้องกันไม่ให้เปลี่ยนค่าละเจ๊ง
เช่น
out.append(data[index][:])
ถ้าไม่ใส่มันจะเอาค่าสุดท้ายของdataเสมอ ไม่เชื่อลองดู
'''
    
