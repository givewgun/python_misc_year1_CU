infile = open('F:\\dropbox\\Dropbox\\python\\prog\\text\\List.txt')
x = []
for line in infile:
    if line.strip() != '' :
        x.append(float(line))
infile.close()
#----------
sum = 0
sum2 = 0
n = len(x)
for e in x:
    sum += e
    sum2 += e**2
mean = sum/n
var = sum2/n - mean**2
#--------------
print( mean , var)
