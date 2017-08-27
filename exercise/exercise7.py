'''
two nested loop: input is two set of numbers, output all possible pairs
in the following format:  read input until end of file

input
1 2 3 
10 20 30

output 
1 10 1 20 1 30 
2 10 2 20 2 30 
3 10 3 20 3 30

10 20 30
1 2 3
11 22 33
4 5 6
111 222 333 444
6 7 8 9
1 1
22 33

hint: keep each input in lists.  using indexing the list to build output.

  rec = input.strip().split()

rec will be a list of each input field
index into rec[i] to get each number.
'''
in_file =open('C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exercise7.txt') #เครื่องล่างใช้ F:\\dropbox\\Dropbox\\python\\prog\\exercise\\text\\exercise7.txt
out_file=open('C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exer7-1.txt', 'w')

while True:

# use readline() to read one line at a time

    x = in_file.readline().strip().split()
    y = in_file.readline().strip().split()

    print(x)

# we stop when there is no input anymore
    if len(x) == 0:
        break

    for i in x:
        xi = int(i)
        out = ""
        for j in y:
            yi = int(j)
            out = out + i + " " + j + " "
        out_file.write(out + '\n')
        if x.index(i) == len(x) - 1:
            out_file.write('\n')
        print(out)
    

in_file.close()
out_file.close()



    
    
