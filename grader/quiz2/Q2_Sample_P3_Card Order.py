order = "A234567890JQK"
file = open("cards.txt","r")
lines = []
for line in file:
    line = line.strip()
    lines.append(line)
#---------
line_num = int(input().strip()) - 1 # change to index in lines list
data = lines[line_num]
state = True
for i in range(len(data)-1): #because we check like a stepping stone _ _ _ _ - _
    if order.find(data[i]) > order.find(data[i+1]):
        state = False
        break
if state == False:
    print("N")
else:
    print("Y")
    
