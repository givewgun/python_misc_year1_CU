file = open(input().strip(), "r")
l = []
#--------- main list
for line in file:
    dat = line.strip().split(";") #"\n" etc when .strip() will -> '' (~empty set)
    if len(dat) > 1:
        id = dat[0]
        name = dat[1] + " " + dat[2]
        score = float(dat[3])+float(dat[4])
        if 80<=score<=100:
            score = "A"
        elif 70<=score<80:
            score = "B"
        elif 60<=score<70:
            score = "C"
        elif 50<=score<60:
            score = "D"
        elif 0<=score<50:
            score = "F"
        il = [id,name,score]
        if len(l) == 0:
            l.append(il)
        else:
            state = True
            for i in range(len(l)):
                if il[0] in l[i]:
                    state = False
            if state == True:
                l.append(il)
student = input().strip()
while student != "-1":
    found = False
    for data in l:
        if data[0] == student:
            print(data)
            found = True
            break
    if found == False:
        print("Not Found")
    student = input().strip()

