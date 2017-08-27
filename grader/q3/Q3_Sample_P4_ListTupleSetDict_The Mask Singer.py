mask2p = dict() #{Crow:[A,B,C]}
#mask_nump = dict() #จน.คนpossiblle:mask
mask_order = []
'''
สร้าง dictที่เก็บค่าหน้ากากกับ[คนที่เป็นได้ ตามลำดับ]
'''
while True:
    data = input().strip().split()#Banana E F G G G G
    if data[0] == 'end':
        break
    else:
        if data[0] not in mask_order: 
            mask_order.append(data[0])
        for p in data[1:]:
            if data[0] not in mask2p:
                mask2p[data[0]] = [p]
            else:
                if p not in mask2p[data[0]]:
                    mask2p[data[0]].append(p)
#print(mask2p)
#---------------------------------------
out = []
'''
ที่ใช้whileเพราะทุกๆครั้งที่เราสรุปว่าหน้ากากนึงเป็นใคร เราต้องเอาแม่งออกพร้อมกับชื่อจริงแม่ง
ละทีนี้พอเอาออกละ เราต้องลบข้อมูลมันออก+ลบชื่อจริงแม่งออกจากหน้ากากอื่นๆด้วย เลยต้องloopว่าเอ๊ะ ยังมีหน้ากากเหลืออยู่ให้ทำใหม่เปล่า
'''
while mask2p != dict():
    #อันนี้คือการเรียงลำดับแบบชื่อน้อยมาก่อน กับถ้าชื่อเท่าเอาหน้ากากที่ใส่มาก่อน ****
    masklen = []
    for mask in mask2p:
        masklen.append((len(mask2p[mask]),mask))
    masklen = sorted(masklen)
    while True:
        sort = True
        for i in range(len(masklen)-1):
            mask_a,mask_b = masklen[i][1],masklen[i+1][1]
            if masklen[i][0] == masklen[i+1][0] and mask_order.index(mask_a) > mask_order.index(mask_b):
                masklen[i],masklen[i+1] = masklen[i+1],masklen[i]
                sort = False
        if sort:
            break          
    #print(masklen) ****
    order = []
    for t in masklen:
        order.append(t[1])
    #print(order)
    #--------------------
    '''อันนี้คือเราเอาเฉพาะคนแรกในorderใหม่เราที่เราทำก่อนหน้าเท่านั้น คนอื่นช่างแม่ง ค่อยคิดต่อเมื่อจบไอห่านี่ละ
พูดง่ายๆก็คือสรุปชื่อจริงคนแรก ตัดแม่งออก คนสองเลื่อนมาเป็นคนแรกแทน ละเริ่มนับ บลาๆใหม่หมด
    '''
    mask = order[0]
    person = mask2p[mask][0]
    out.append([mask,person])
    mask2p.pop(mask)
    for key in mask2p:
        if person in mask2p[key]:
            mask2p[key].remove(person)
    mask_order.remove(mask)

for  c in out:
    print(" ".join(c))
    
#sortแบบdict เอาไปแทนตรง *** bubbleได้
'''s_len = sorted(masklen.keys())
new_order = []
for key in s_len:
    if len(masklen[key]) == 1:
        mask = list(masklen[key])[0]
        new_order.append(mask)
        mask_order.remove(mask)
    else:
        for m in mask_order:
            if m in masklen[key] and len(masklen[key]) > 0:
                new_order.append(m)
                masklen[key].remove(m)
                
print(new_order)
'''               

