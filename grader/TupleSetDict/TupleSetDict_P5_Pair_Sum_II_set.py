num = [int(e) for e in input().strip().split()]
sum = int(input().strip())
has_pair = 0
sum_remain = {sum - num[0]} #แนวคิดแบบหาตัวที่ต้องบวกให้ได้ตามที่ต้องการ ละเก็บไว้ ไล่ไปเรื่อยๆ ภ้าเจอแปลว่าเข้าคู่กับตัวที่เคยผ่านมาละ
for i in range(1,len(num)):
    #print(sum_remain)
    #print(num[i])
    #print("------------")
    if num[i] in sum_remain:
        has_pair += 1
    tmp = {sum - num[i]}
    sum_remain.update(tmp)
print(has_pair)
