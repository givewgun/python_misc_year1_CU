l = sorted([ int(e) for e in input().strip().split()])
recur = ["a"] #ใช้ a เพราะถ้าเปรียบเลขตัวแรกจะไม่เท่าแน่นอน
state = False
if len(l) == 1:
    print(l[0])
    exit(0)
for i in range(len(l)-1): #[1] [1]
    if l[i] == l[i+1] and l[i] != recur[-1]: #ใช้แบบตัวๆจะลดได้เยอะเพราะไม่ต้องไล่ใหม่ ละคือเราเรียงเลขแล้วเพราะฉะนั้นเช็คซ้ำก็เช็คแค่ตัวสุดท้าย
        recur.append(l[i])
    elif l[i] != l[i+1] and l[i] != recur[-1]:#t = nไม่งั้นถ้าวนลูป2ลูปละจะtime out @ช่น in count for ซ้อนๆกัน!!!
        print(l[i])
        state = True
        break
if state == False:
    print("NONE")
'''
for i in range(len(l)-1): #[1] [1] *** t=n
    if l[i] == l[i+1] and l[i] not ***in*** recur: #slow t=n*n
        recur.append(l[i])
    elif l[i] != l[i+1] and l[i] not ***in*** recur:
        print(l[i])
        state = True
        break
if state == False:
    print("NONE")
'''        
    
    
