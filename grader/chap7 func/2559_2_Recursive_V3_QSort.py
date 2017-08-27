import random
def qsort( d ):
 if len(d) < 1:return d # ถ้า d มีข้อมูลไม่เกิน 1 ตัว ก็คืน d กลับไปได้เลย เพราะเรียงอยู่แล้ว
 p = d[random.randint(0,len(d)-1)] # สุ่มเลือกข้อมูลใน d มาหนึ่งตัว เก็บในตัวแปร p
 le = [ i for i in d if i < p ] # สร้าง list ชื่อ le เก็บข้อมูลใน d ทุกตัวที่มีค่าน้อยกว่า p (เขียนด้วย list comprehension ใช้บรรทัดเดียว)
 eq = [ i for i in d if i == p ] # สร้าง list ชื่อ eq เก็บข้อมูลใน d ทุกตัวที่มีค่าเท่ากับ p (เขียนด้วย list comprehension ใช้บรรทัดเดียว)
 mo = [ i for i in d if i > p ]# สร้าง list ชื่อ mo เก็บข้อมูลใน d ทุกตัวที่มีค่ามากกว่า p (เขียนด้วย list comprehension ใช้บรรทัดเดียว)
 le = qsort(le) # เรียงล าดับข้อมูลใน le ด้วย qsort เก็บผลใส่ le
 mo = qsort(mo) # เรียงล าดับข้อมูลใน mo ด้วย qsort เก็บผลใส่ mo
 return le+eq+mo # เมื่อน า le ต่อกับ eq ต่อกับ mo ย่อมได้ข้อมูลเรียงล าดับจากน้อยไปมาก ก็คืนผลการต่อนี้กลับเป็นผลลัพธ์
d = [int(e) for e in input().split()]
d = qsort(d)
print(' '.join([str(e) for e in d]))
