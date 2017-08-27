file = open("score.txt","r")
id = []
score = []
s = ""
for line in file:
    line = line.strip().split()
    id.append(line[0])
    score.append(line[1])
n = input().strip()
while n != "-1":
    if n not in id:
        s += "Not Found" +"\n"
    else:
        s += score[id.index(n)] + "\n"
    n = input().strip()
print(s.strip())
    
