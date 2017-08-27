#MIN MAX
'''
d = int(input())
max = d
min = d
d = int(input())
if d > max :
 max = d
d = int(input())
if d > max :
 max = d
print(max)
'''
for i in range(6):
    if i == 0:
        d = float(input())
        min = d
        max = d
    else:
        d = float(input())
        if d > max:
            max = d
        elif d < min:
            min = d
print(min,max)
