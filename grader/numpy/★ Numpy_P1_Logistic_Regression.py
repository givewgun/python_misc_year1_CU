import numpy as np
data = np.array([[15,3.78],
                 [29,2.0],
                 [10,2.5],
                 [25,2.85],
                 [30,3.96]])
def logit_pi(n):
    return -3.98 + 0.2*data[n][0] + 0.5*data[n][1]
def p_xi(n):
    return 1 / (1+np.exp(-logit_pi(n)))
n = int(input())
if n > np.shape(data)[0] or n < 1:#1คน shape คือ 1,2
 print('Error')
elif p_xi(n-1) > 0.5:
 print('True')
else:
 print('False')
