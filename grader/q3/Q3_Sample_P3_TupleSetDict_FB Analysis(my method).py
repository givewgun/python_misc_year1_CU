user2page = dict()#{user:page}
page2user = dict()#{page:user}
#----
n = int(input().strip())
for i in range(n):
    data = input().strip().split()#Sukree Food Panda Movie
    if data[0] not in user2page:
        user2page[data[0]] = set(data[1:])
    else:
        user2page[data[0]].update(data[1:])
    for p in data[1:]:
        if p not in page2user:
            page2user[p] = {data[0]}
        else:
            page2user[p].add(data[0])
#----
while True:
    x = input().strip().split()
    if len(x) == 1: break
    elif x[0] == 'common' and x[1] == 'page':#common page Somchai Sukree
        if x[2] not in user2page:
            ans = set()
        else:
            ans = user2page[x[2]]
        for name in x[3:]:
            if name not in user2page:
                ans = ans.intersection(set())
            else:
                ans = ans.intersection(user2page[name])
        print(len(ans))
    elif x[0] == 'common' and x[1] == 'user':#common user Panda Food
        if x[2] not in page2user:
            ans = set()
        else:
            ans = page2user[x[2]]
        for page in x[3:]:
            if page not in page2user:
                ans = ans.intersection(set())
            else:
                ans = ans.intersection(page2user[page])
        print(len(ans))    
    elif x[0] == 'similar' and x[1] == 'user':#similar user Somchai
        if x[2] not in user2page:
            ans = set()
        else:
            ans = user2page[x[2]]
        sim = dict()#{2:user}
        for name in user2page:
            if name != x[2]:
                value = len(ans.intersection(user2page[name])) / len(ans.union(user2page[name]))
                if value not in sim:
                    sim[value] = {name}
                else:
                    sim[value].add(name)
        s_value = sorted(sim.keys(),reverse= True)#เรียงค่าsimจากมากไปน้อย
        out = []
        for i in s_value:
            out.extend(sorted(sim[i]))#เรียงชื่อในกรณีที่ค่าsimนั้นเท่ากัน
        print(out[0])
    elif x[0] == 'similar' and x[1] == 'page':#similar page MaewMeow
        if x[2] not in page2user:
            ans = set()
        else:
            ans = page2user[x[2]]
        sim = dict()#{2:user}
        for page in page2user:
            if page != x[2]:
                value = len(ans.intersection(page2user[page])) / len(ans.union(page2user[page]))
                if value not in sim:
                    sim[value] = {page}
                else:
                    sim[value].add(page)
        s_value = sorted(sim.keys(),reverse= True)#เรียงค่าsimจากมากไปน้อย
        out = []
        for i in s_value:
            out.extend(sorted(sim[i]))#เรียงชื่อในกรณีที่ค่าsimนั้นเท่ากัน
        print(out[0])        

