infile = open('data.txt')
lines = infile.readlines() #into list with a line per element
n = int(input().strip())
i = 0
state = False
for line in lines:
    if 'Name' in line:
        i += 1
        if i == n:
            print(line[line.find(':')+2:].strip())
            state = True
if state == False:
    print('Not Found')


        
    

