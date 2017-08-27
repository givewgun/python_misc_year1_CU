#[0,[1,[2,[3,[4,5],6],7],8],[9,10]]
def sumlist(x):
    sum = 0
    if type(x) == int: sum += x
    elif type(x) == list:
        if x == []: sum += 0
        else:
            for i in x:
                sum += sumlist(i)
    return sum
        

print(sumlist(eval(input().strip()))) # do not remove this line 
