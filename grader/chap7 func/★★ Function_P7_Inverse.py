import math
def f(x): #f(x) = x^2 + x^2/x *2 +3 = x^2 +2x +1 +2
    k = 0
    for i in range(1,2*x,2):
        k += i
    #print(k)
    for j in range(k):
        if j%x==0:
            k += 2
    #print(k)
    return k+3
# output ของฟังก์ชันจะเป็นจ านวนเต็มบวก
def f_inv(x):#f-1(x) = sqrt(x-2) -1
    return int(math.sqrt(x-2) - 1)
print(eval(input().strip()))
