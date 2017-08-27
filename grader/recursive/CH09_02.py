def isSorted(L):
 if len(L)<=2:
     return True
 if L[0]<=L[1]<=L[-1]:
     return isSorted(L[1:])
 if L[0]>=L[1]>=L[-1]:
     return isSorted(L[1:])
 return False

n = int(input())
L = [int(e) for e in input().split()]
if isSorted(L):
 print('true')
else:
 print('false')
