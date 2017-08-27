import numpy as np
n = int(input().strip())
price = np.array([[int(input().strip().split()[1]) for i in range(n)]])
#print(price)
sell = np.array([[int(e) for e in input().strip().split()[1:]] for i in range(n)], dtype = float)
#print(sell)
for p in price.dot(sell)[0]:
    print(p)
