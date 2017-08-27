#exercise4
in_file =open('C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exercise4.txt')
out_file=open('C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exer4.txt', 'w')
count = 0
for line in in_file:
    #print(line)
    for c in line.strip() :
        if int(c) == 1:
            count += 1
    print(count)
    out_file.write(str(count) + '\n')
    count = 0

in_file.close()
out_file.close()

    
    
    


