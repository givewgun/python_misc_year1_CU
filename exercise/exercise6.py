'''
The inventory consists of T-shirt with two colors {red,blue} and two sizes {big,small}.  The input file has the following form:

product_ID  color  size

1234  red  big
1246  blue small
....

write a program to read the input file and count the inventory of each category:
{red-big, red-small, blue-big, blue-small} and output that count.

for example
input6.txt

input
346  red big
2678  blue small
135  blue small
467  red big

output
2 0 0 2
'''
in_file =open('F:\\dropbox\\Dropbox\\python\\prog\\exercise\\text\\exercise6.txt') #เครื่องล่างใช้ C:\\Users\\Administrator.BULEZ4LEYH5EFRE\\Dropbox\\python\\prog\\exercise\\text\\exercise6.txt
out_file=open('F:\\dropbox\\Dropbox\\python\\prog\\exercise\\text\\exer6.txt', 'w')
lib = {'red-big':0 , 'red-small':0 ,'blue-big':0, 'blue-small':0}
for line in in_file:
    line_set = line.strip().split()
    print(line_set)
    keyword = line_set[1] + '-' + line_set[2]#สร้างชื่อให้เหมือนกับในlib
    if keyword in lib.keys():
        lib[keyword] += 1
for key,value in sorted(lib.items()): #ตัวหน้าคือคีย์ หลังคือ ค่าของคีย์
    print(key ,value)
    out_file.write(key +' ' +str(value)+ '\n')
in_file.close()
out_file.close()
