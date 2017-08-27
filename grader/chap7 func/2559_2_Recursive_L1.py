def A(x):
 if len(x)==0 : return x
 return A(x[1:]) + x[0]
def B(x):
 if len(x)==0 : return x
 return x[-1] + B(x[:-1])
def C(x):
 if len(x)==0 : return 0
 m = len(x)//2
 return C(x[:m]) + x[m]+ \
 C(x[m+1:])
def D(x):
 if len(x)==0: return 0
 m = len(x)//2
 return D(x[:m]) + \
 D(x[m:])
def E(x):
 if len(x)==0 : return 0
 return x[0] + E(x[1:])
def F(x):
 if len(x)==0 : return x
 return x[0] + F(x[1:])
def G(x):
 if len(x)==0 : return x
 return G(x[:-1]) + x[-1]
def H(x):
 if x==0 : return True
 return J(x-1)
def J(x):
 if x==0 : return False
 return H(x-1)
def M(x):
 if x==0 : return True
 elif x==1 : return False
 return M(x-1)
def N(x):
 if x==0 : return False
 elif x==1 : return True
 return N(x-1)
def P(x):
 if len(x)==0 : return x
 return x[-1]+P(x[1:-1])+\
 x[0]
print(A("ABCD"))
print(B("ABCD"))




print(P("ABCD"))



