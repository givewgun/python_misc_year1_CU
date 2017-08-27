class roman:
  
  def __init__(self, r):
    self.r = r
    
  def __lt__(self, rhs):
    return int(self) < int(rhs)
    
  def __str__(self):
    return self.r
    
  def __int__(self):
    r = self.r
    num = 0
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    idx = r.find('IV')
    if idx >= 0:
      num += 4
      r = r[:idx] + r[idx+2:]
    idx = r.find('IX')
    if idx >= 0:
      num += 9
      r = r[:idx] + r[idx+2:]
    idx = r.find('XL')
    if idx >= 0:
      num += 40
      r = r[:idx] + r[idx+2:]
    idx = r.find('XC')
    if idx >= 0:
      num += 90
      r = r[:idx] + r[idx+2:]
    idx = r.find('CD')
    if idx >= 0:
      num += 400
      r = r[:idx] + r[idx+2:]
    idx = r.find('CM')
    if idx >= 0:
      num += 900
      r = r[:idx] + r[idx+2:]
    for x in r:
      num += d[x]
    return num
  
  def __add__(self, rhs):
    s = ''
    n = int(self) + int(rhs)
    k = n//1000
    if k > 0:
      n -= k*1000
      s += 'M'*k
    if n >= 500:
      s += 'D'
      n -= 500
    if n//400 == 1:
      s += 'CD'
      n -= 400
    k = n//100
    if k > 0:
      s += 'C'*k
      n -= k*100
    if n//90 == 1:
      s += 'XC'
      n -= 90
    k = n//50
    if k > 0:
      s += 'L'*k
      n -= 50*k
    if n//40 == 1:
      s += 'XL'
      n -= 40
    k = n//10
    if k > 0:
      s += 'X'*k
      n -= 10*k
    if n//9 == 1:
      s += 'IX'
      n -= 9
    k = n//5
    if k > 0:
      s += 'V'*k
      n -= 5*k
    if n//4 == 1:
      s += 'IV'
      n -= 4
    if n > 0:
      s += 'I'*n
    return roman(s)
    
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
