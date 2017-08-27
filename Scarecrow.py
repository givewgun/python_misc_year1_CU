#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
field =  str(raw_input("enterfield a=waste b=crops \n"))
field_1 = list(field)
count = 0
start = 0
for i in range(start,len(field_1)):
    if field_1[i] == "a":
       if i < len(field_1)-1 and field_1[i-1] != 'b':
           field_1[i+1] = 'b'
           count +=1
           start = i+2
    elif field_1[i] == 'b':
       start = i+1
print("".join(field_1) , count)
