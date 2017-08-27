'''
สรุป : เรา sort list of tuples หรือ list of lists ได้
การเปรียบเทียบของ tuple ว่า (a,b) น้อยกว่า (c,d) ก็เมื่อ
a < c หรือไม่ a==c and b < d
เช่น (1,2) น้อยกว่า (3,1) (1,2) น้อยกว่า (1,3) ไล่จากหน้า

ถ้าโจทย์ให้ sort แบบแปลก ๆ เช่น
x = [ (1,'a'), (2,'b'), (1,'c'), (3,'a') ]
อยากให้ sort โดยเรียงตัวแรกใน tuple จากมากไปน้อย ถ้าตัวแรกเท่า ขอเรียงตัวหลังจากน้อยไปมาก
ก็ง่าย ๆ โดยสร้าง list ใหม่
x = [ (-a,b) for (a,b) in x ]
แล้วก็ x.sort() ได้
x = [ (-3,'a'), (-2,'b'), (-1,'a'), (-1,'c') ]
เอาลบออกก็ได้ตามต้องการ
x = [ (-a,b) for (a,b) in x ]
x = [ (3,'a'), (2,'b'), (1,'a'), (1,'c') ]
'''
eng = "abcdefghijklmnopqrstuvwxyz"
n = int(input().strip())
alpha = [ [0 for i in range(26)]+["s"] for j in range(n)]# = [[0,0,..],"word"]
for i in range(n):
    s = input().strip()
    for c in s:
        c = c.lower()
        alpha[i][eng.find(c)] += 1
    alpha[i][-1] = s
alpha.sort()
#----
for i in range(n):
    print(alpha[i][-1])
