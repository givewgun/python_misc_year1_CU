def copylist( x ):#a = [1,2,[3,4],[[5,6],8]]
    if type(x) != list:
        y = x
    else:
        y = list()
        for i in x:
            y.append(copylist(i))
    return y
        
exec(input().strip()) # do not remove this line
