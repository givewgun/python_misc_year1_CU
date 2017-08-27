infile = open('score.txt','r')
id = input().strip()
state = False
for line in infile:
    d = line.strip().split()
    if d[0] == id:
        print(d[1])
        state = True
        break
if state == False:
    print('Not Found')
    
