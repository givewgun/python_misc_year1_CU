#คะแนนมากไปน้อย ชื่อน้อยไปมาก
def compare(a, b):#('593...', 3), ('593...', 4)
    if a[1] < b[1]:
        return True
    elif a[1] == b[1] and a[0] > b[0]:# ถ้าคะแนนเท่า แต่ชื่อมันดันมาหลังตัวถัดไป ต้องให้สลับ
        return True
n = int(input().strip())
d = []
for i in range(n):
    x, y = input().strip().split()
    d.append((x, float(y))) #[('593...', 3), ('593...', 4)]
for k in range(n-1):
    for i in range(n-1):
        if compare(d[i], d[i+1]):#เช็คtuple ถ้ามันเรียงผิด ต้องสลับ
            d[i], d[i+1] = d[i+1], d[i]
for i in d:
    print(i[0], i[1])
