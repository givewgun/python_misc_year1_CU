file = open(input().strip(), "r")
l = []
#fruit list-------
for line in file:
    line = line.strip().split()
    fruit = line[0]
    name = line[1]
    if len(l) == 0:
        l.append([fruit,[name]])
    else:
        recur = False
        for i in range(len(l)):
            if fruit == l[i][0]:
                l[i][1].append(name)
                recur = True
                break
        if recur == False:
            l.append([fruit,[name]])
#most favourite
max = 0
fav = ""
for data in l:
    if len(data[1]) > max: #data[1] is name of who likes
        max = len(data[1])
        fav = data[0]
print(l)
print("The most favorite fruit is " + fav)
