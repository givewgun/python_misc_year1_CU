#Input is 3 numbers.  Write a program using a decision tree to find the
#max number. Each line of input file has 3 numbers.Output the max number.
#Read input file until the end of file.
in_file =open('C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exercise5.txt')
out_file=open('C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exer5.txt', 'w')

#hint
#Use input().strip().split()  to get three numbers.  The result is a list.
for line in in_file:
    List = line.strip().split()
    print(List)
    n = 1
    highest = int(List[0])
    while n < len(List):
        if int(List[n]) > highest:
            highest = int(List[n])
        n += 1
    print(highest)
    out_file.write(str(highest) + '\n')

in_file.close()
out_file.close()
                   
    

