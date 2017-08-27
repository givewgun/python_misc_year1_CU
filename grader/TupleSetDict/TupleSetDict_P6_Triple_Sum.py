num,query = [int(e) for e in input().strip().split()]
list_n = [int(e) for e in input().strip().split()]
list_q = [int(e) for e in input().strip().split()]
sum_remain = {list_n[0] + list_n[1]}# sum ของสองตัวใดๆ แนวคิดคล้ายข้อที่แล้ว แค่ต่างว่า sum - 1ต1ว = 2ตัวที่เหลือบวกกัน
out = ["NO" for k in range(query)]
for i in range(2,num):#ไล่ดาต้าไปทีละตัวๆว่าตัวนี้เนี่ย มันสามารถบวกกับสองตัวใดๆที่ผ่านมาละได้คำตอบ(ที่จะไล่ไป)ไหม
    for j in range(query):#ไล่คำตอบทุกตัว ใน ดาต้า1ตัวก่อน
        if list_q[j] - list_n[i] in sum_remain:
            out[j] = "YES"
    next_sum = [list_n[i] + list_n[k] for k in range(i)] #เอาตั้วที่มีอยู่บวกกับตัวก่อนหน้า เพื่อเอาไปใช้ต่อ
    sum_remain.update(next_sum)
for i in out:
    print(i)

    
            
