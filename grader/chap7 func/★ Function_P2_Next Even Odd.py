#int ปัดเข้าหา0
import math
def nextEven(f):
    #2.5->3+1->4
    #3.5->4 +1->5 -3.5->-2+1-> -1
    n = math.ceil(f)
    if n % 2 == 0:
        return n
    else:
        return n+1
    # write your code here
def nextOdd(f):
    #3.5->4 +1->5 -3.5->-2+1-> -1
    n = math.ceil(f)
    if n % 2 == 0:
        return n+1
    else:
        return n
    # write your code here
while True:
    x = float(input())
    if x < 0:
        break
    even = nextEven(x)
    odd = nextOdd(x)
    print( (even, odd) )
