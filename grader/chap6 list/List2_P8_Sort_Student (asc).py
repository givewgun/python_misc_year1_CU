file = open("score.txt", "r")
id = []
for line in file:
    line = line.strip().split()
    id.append(int(line[0]))
id = sorted(id)
for i in id:
    print(i)
