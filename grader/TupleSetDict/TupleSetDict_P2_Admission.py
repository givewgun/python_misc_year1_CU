num = int(input().strip())
courses = dict()
for i in range(num):
    id,c1,c2,c3,c4 = [ e for e in input().strip().split(", ")]#id อยู่index1
    if c1 not in courses:
        courses[c1] = [id]
    elif c1 in courses:
        courses[c1].append(id)
    if c2 not in courses:
        courses[c2] = [id]
    elif c2 in courses:
        courses[c2].append(id)
    if c3 not in courses:
        courses[c3] = [id]
    elif c3 in courses:
        courses[c3].append(id)
    if c4 not in courses:
        courses[c4] = [id]
    elif c4 in courses:
        courses[c4].append(id)

    
progs = [e for e in input().strip().split(", ")]
for p in progs:
    if p in courses:
        print(p,"->",", ".join(courses[p]))
    else:
        print(p,"->","Not found")
    
