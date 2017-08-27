n = int(input().strip())
students = dict()

for i in range(n):
    data = [e for e in input().strip().split()]
    name = data[0]
    students[name] = data[1:],set(data[1:]) #setไว้เช็คintersect จะได้เร็วๆ
#--------
find = set(e for e in input().strip().split())#ไว้intersectเช็คเป็น คนๆ
#--------
out = dict()#เก็[คนที่ตรงเป็นdict (valueเป็นlistเพราะไม่งั้นมันเรียงบรรทัดมั่ว)
for name in students:
    if students[name][1].intersection(find) == find: #'Pim': (['C', '99', 'CP'], {'CP', '99', 'C'}
        out[name] = students[name][0]
if out == dict():
    print("Not Found")
    exit(0)
#----------
else:
    name_s = sorted(out.keys())#เรียงชื่อตามพจนานุกรม ละค่อยปริ้นตามลำดับ
    for n in name_s:
        print(n ," ".join(out[n]))
