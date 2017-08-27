#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
#pyramid
'''
n=3                ช่องว่าง                               (range)
      1               4 (3-1)*2                             0
    1 2 3             2 ((3-1)-1)*2                         1
  1 2 3 4 5           0 ((3-1)-2)*2                         2
1 2 3 4 5 6 7
                     n-(n-1)    

'''
level = int(input('number of pyramid floor : '))
level_new = (level - 1)*2
start = 1

for i in range(level):
    lvl = level_new -2*i
    s=''
    end = (i+1)*2
    s += ' '*lvl
    for j in range(1,end):
        s += str(j) +' '
        
    print(s)

    
    
