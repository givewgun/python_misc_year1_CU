def row_number(t, e): # return row number of t containing e (top row is row #0)
    #[ [1,7,2,3], [6,0,8,4], [5,9,10,11], [13,14,15,12] ]
    for i in range(len(t)):
        if e in t[i]:
            return i       
def flatten(t): # return a list of ints converted from list of lists of ints t
    #จาก [ [1,2,0],[3,5,6],[4,7,8] ] ก็เปลี่ยนเป็น [1,2,3,5,6,4,7,8] ตัด0 ทิ้ง
    n = []
    for l in t:
        for i in l:
            if i != 0:
                n.append(i)
    return n
        
def inversions(x): # return the number of inversions of list x
    #คือจ านวนคู่ของข้อมูลใน list of ints ว่า มีกี่คู่ที่ตัวซ้ายมากกว่าตัวขวา (5,6)
    n = []
    c = 0
    for i in range(len(x)):
        for j in range(i,len(x)):
            n.append((x[i],x[j]))
    for t in n:
        if t[0] > t[1]:
            c += 1
    return c
def solvable(t):
    # return True if tiling t (list of lists of ints) is solvable
    # otherwise return False
    inv = inversions(flatten(t))
    row_pos = row_number(t, 0)
    if len(t) %2 != 0 and inv%2 == 0:
        return True
    elif len(t)%2 == 0:
        if inv%2 != 0 and row_pos%2 == 0:
            return True
        elif inv%2 == 0 and row_pos%2 != 0 :
            return True
    return False
        

exec(input().strip()) # do not remove this line
