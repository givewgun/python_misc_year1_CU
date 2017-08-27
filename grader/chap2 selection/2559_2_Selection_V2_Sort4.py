#จงเขียนโปรแกรมที่เรียงลําดับคาในตัวแปร 4 ตัว จากนอยไปมาก ที่ทํางานตาม flowchart ขางขวานี้ 
a,b,c,d = [int(input()) for i in range(4)]
if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if c>d:
    c,d = d,c
if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a
print(a,b,c,d)

