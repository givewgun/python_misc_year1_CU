n = int(input().strip())
pop = dict()#dict รวม คำขึ้นต้นสองคำแรก
for i in range(n):
    data = input().strip().split()[1]
    f_two = data[:2].lower()
    if f_two not in pop:
        pop[f_two] = [data]#ให้valueเป็นlistดีกว่า เพราะเวลาprintมันจะตามลำดับ ก่อน ไปหลังเลย ใช้dict แม่งชอบมีปัญหา
    else:
        pop[f_two].append(data)


pop_len = dict()
for key in pop:
    pop_len[key] = len(pop[key])

before = set()
for key in pop_len:
    if pop_len[key] == max(pop_len.values()):
        before.update({key.lower()})
before = min(before)

print(before + "\n" + str(pop_len[before]) + "\n" + "\n".join(pop[before]))
        
    
