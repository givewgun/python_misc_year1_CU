def gcd(x,y):
  if x%y == 0: return y
  return gcd(y,x%y)
  
class Fraction:
  def __init__(self,a,b):
    self.numerator = a
    self.denominator = b
    
  def __str__(self):
    return str(self.numerator) + '/' + str(self.denominator)
  
  def simplify(self):
    g = gcd(self.numerator,self.denominator)
    return Fraction(self.numerator//g,self.denominator//g)
    
  def add(self,other):
    u1 = self.numerator
    u2 = other.numerator
    d1 = self.denominator
    d2 = other.denominator
    f = Fraction(u1*d2 + u2*d1, d1*d2)
    f = f.simplify()
    return f
  
  def multiply(self,other):
    ans_numer = self.numerator * other.numerator
    ans_denom = self.denominator * other.denominator
    return Fraction(ans_numer,ans_denom).simplify()
 
a,b,c,d = [int(e) for e in input().strip().split()]
fraction1 = Fraction(a, b)
fraction2 = Fraction(c, d)
print(fraction1.add(fraction2))
print(Fraction.multiply(fraction1,fraction2))