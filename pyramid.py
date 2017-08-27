#pyramid
'''
n=3                ช่องว่าง  lvl**                  floor           floor_1 start    end = (floor_1+1)**2 + 1    range(math)
      1               4 (3-1)*2               1                 0         1              2                        [1]
    2 3 4             2 ((3-1)-1)*2           2                 1         2             5                         [2,4]
  5 6 7 8 9           0 ((3-1)-2)*2           3                 2         5             10                        [5,9]
0 1 2 3 4 5 6 
                     [(n-1)-floor]*2    

'''
level = int(input('number of pyramid floor : '))
level_new = (level - 1)*2
start = 1

for floor_1 in range(level):
    lvl = level_new -2*floor_1 #**
    s=''
    end = (floor_1+1)**2 + 1
    s += ' '*lvl
    for j in range(start,end):
        s += '$' +' '
        start = end
    print(s)

    
    
