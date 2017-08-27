course = dict()
while True:
    data = input().strip().split()
    if data[0] == "-1":
        break
    else:
        for c in data[1:]:
            if c not in course:
                course[c] = {data[0]} # ยังไม่มีข้อมูลในดิค เพิ่มตนแรกไปก่อน
            else:
                course[c].update({data[0]})

c1,c2 = set(e for e in input().strip().split())
if c1 in course and c2 in course:
    both = len( course[c1].intersection(course[c2]) ) #ตัวซ้ำ 
    one = ( len(course[c1])-both ) + ( len(course[c2])-both ) #AuB = A+B- AnB, A_pure = A- AnB
    print(both,one,both+one)
elif c1 in course and c2 not in course:
    both = 0
    one = len(course[c1])
    print(both,one,one)
elif c1 not in course and c2 in course:
    both = 0
    one = len(course[c2])
    print(both,one,one)
elif c1 not in course and c2 not in course:
    print(0,0,0)


