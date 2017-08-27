import numpy as np


def A_n(A,n):#B = np.sign(A+A^2+...+A^n-1)
    if n-1 == 0:#
        return A
    else:
        return A.dot(A_n(A,n-1))

def main():
    n = int(input().strip())
    A = np.array([[int(e) for e in input().strip().split()] for i in range(n)])
    temp = 0
    for i in range(1,n+1):
        temp += A_n(A,i)
        #print(temp)
    B = np.sign(temp)
    for row in B:
        row = map(str,row.tolist())# array.tolist() -> numpy to list
        print(" ".join(row).strip())

      
    
main()
