class Complex:
  def __init__(self, a, b):
    self.r = a
    self.i = b
  def __str__(self):
    if self.i == 0:
      return str(self.r)
    elif self.r == 0:
      if self.i == 1: return 'i'
      elif self.i == -1: return '-i'
      return str(self.i) + 'i'
    elif self.i > 0:
      return '{}+{}i'.format(self.r, self.i if self.i != 1 else '')
    return '{}{}i'.format(self.r, self.i if self.i != -1 else '-')
  def __add__(self, rhs):
    return Complex(self.r+rhs.r, self.i+rhs.i)
  def __mul__(self, rhs):
    return Complex(self.r*rhs.r - self.i*rhs.i, self.r*rhs.i + self.i*rhs.r)
  def __truediv__(self, rhs):
    a, b, c, d = self.r, self.i, rhs.r, rhs.i
    return Complex((a*c + b*d)/(c**2 + d**2), (-a*d + b*c)/(c**2 + d**2))
  
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
    