#---create dept and it's capacity
n = int(input().strip())
dept = dict()
dept_cap = dict()
for i in range(n):
    data = input().strip().split()  #CP 1
    dept[data[0]] = []
    dept_cap[data[0]] = int(data[1])#เก็บจนใคนที่รับได้ไว้อันดับแรก
#----sort rank
m = int(input().strip())
scores = dict()
for i in range(m):
    data = input().strip().split()#59301234521 23.6 PE CP MT CHE
    s = data[1]
    data.remove(s)
    scores[float(s)] = data
rank = sorted(scores.keys(), reverse = True)
#--------- check เป็ฯคนๆตามrankว่าเต็มยังบลาๆ 
out = dict()
for s in rank:# ex 19.4: ['59300002121', 'CHE', 'CP', 'ME', 'CP']
    for i in range(1,5):#อันดับภาค
        id = int(scores[s][0])
        choose = scores[s][i]
        if len(dept[choose]) < dept_cap[choose]:
            dept[choose].append(id)
            out[id] = choose
            break
s_id = sorted(out.keys())
for c in s_id:
    print(c,out[c])


