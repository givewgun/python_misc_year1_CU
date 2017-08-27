#ISBN
import math
num_9 = input()
total_9 = 0
for i in range(9):
    total_9 += int(num_9[i]) * (10-i)
# total_9 + n10 = 11(k) (k = ceiling total_9/11)
k = math.ceil(total_9 / 11) 
# n10 = 11(k) - total_9
n10 = 11*(k) - total_9
print(num_9 + str(n10))
    
