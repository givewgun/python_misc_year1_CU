def h(n):
 if n<2:
     return n
 return 2*h(n-2) + 1
def g(n):
 if n<3:
     return 1
 s = 0
 for k in range(n):
     s += g(k)
 return s
def f(n,k):
 if k==n:
     return n
 return 2*f(n,k+1)-3
def m(n):
 if n==1 : return 0
 return 1+m(n//2)

print(g(4))
'''
h(7)=2*h(5) + 1 = 15
h(5)=7
2*h(3) +1
2*(2*h(1)+1)+1
2*(2*1 +1)+1

g(4) = s+= g(k) for k in range(4)
g(4) = g(0)+g(1)+g(2)+g(3)
    = g(0)+g(1)+g(2) + g(0)+g(1)+g(2) = 6
g(6) = g(0)+g(1)+g(2)+g(3) + g(4) + g(5)
    = 6 + g(0)+g(1)+g(2)+g(3) + g(0)+g(1)+g(2)+g(3)+g(4)
    = 6+6+6+6

f(2,0) = 2f(2,1) -3 = 2(2*f(2,2)-3) -3 = 2(2*2-3)-3 =-1
f(4,2) = 2f(4,3) -3 = 2(2*f(4,4)-3) -3 = 2(2*4-3)-3 =7
f(4,1) = 2f(4,2)-3 = 2*7 -3 = 11

m(2) = 1+m(1) = 1+0 = 1
m(8)  = 1+m(4) = 1+(1+m(2)) = 1 + (1+1) = 3
m(100) = 1+m(50)=1+1+m(25)=1+1+1+m(12)=1+1+1+1+m(6)=1+1+1+1+1+m(3)=1+1+1+1+1+1+m(1)
'''