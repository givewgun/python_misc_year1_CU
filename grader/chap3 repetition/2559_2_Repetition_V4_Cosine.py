import math
x = float(input())
cos = 0
k = 0
term = (((-1)**k) * (x**(2*k)))/(math.factorial(2*k))
while abs(term) > 1e-8: #ในโจทย์ไม่ได้บอกแต่แม่งต้องใส่
    k += 1
    term = (((-1)**k) * (x**(2*k)))/(math.factorial(2*k))
print(cos)
    
