import numpy as np
n = int(input().strip()) - 3
for i in range(3):#nonsense
    d = input()
score = np.array([[int(e) for e in input().strip().split(",")[1:]] for i in range(n)], dtype = float)
#print(np.sum(score,axis = 1))
for s in np.sum(score,axis = 1):
    print(s)
