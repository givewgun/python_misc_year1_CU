#Mode
n = int(input('Enter the number of data : '))
data = []
for i in range(n):
    x = float(input(' >> '))
    data.append(x)
#--------------------------------
counts = [0]*n         #data = [1,1,2,2,2,1,2,3]
for k in range(n):     #count  [3,3,4,4,4,3,4,1] เcount[i] เก็บจำยวนdata[i]
    for j in range(n) :
        if data[k] == data[j]:
            counts[k] += 1 
maxI = 0                         #data = [1,1,2,2,2,1,2,3] 
for i in range(len(data)):                       
    if counts[maxI] < counts[i]:
        maxI = i
print('mode = ',data[maxI])
            
    
