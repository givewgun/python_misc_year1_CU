met,dimen = [int(e) for e in input().strip().split()]
m = []
for i in range(dimen):
    m.append([int(e) for e in input().strip().split()])

t = 0
if met == 0:#low triangle
    for i in range(0,dimen):
        if i == 0:
            t += (m[0][0])
        else:
            t += sum(m[i][:i+1])
elif met == 1:#high triangle
    for i in range(0,dimen):
         t += sum(m[i][i:])
print(t)
        
