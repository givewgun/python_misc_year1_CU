pile = []
while True:
    m = [e for e in input().strip().split()] #m == method xxxx (xxxx xxxx)
    if len(m) > 2: #return py 101
        m = [m[0] ," ".join(m[1:])]
    
    if m[0] == 'end':
        break
    else:
        if m[0] == 'return':#return bookname
            pile.append(m[1])
            print(len(pile))
        elif m[0] == 'shelf':
            if pile == []:
                print("no book")
            else:
                last = pile[-1]
                print(last)
                pile = pile[:-1]
        elif m[0] == 'top':
            if pile == []:
                print("no book")
            else:
                last = pile[-1]
                print(last)
        elif m[0] == 'list':
            print(pile)

            
            
