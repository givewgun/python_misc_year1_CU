class piggybank:
  def __init__(self):
    self.coins = [0]*4
  def add1(self, n):
    self.coins[0] += n
  def add2(self, n):
    self.coins[1] += n
  def add5(self, n):
    self.coins[2] += n
  def add10(self, n):
    self.coins[3] += n
  def __int__(self):
    return sum([self.coins[i]*(1, 2, 5, 10)[i] for i in range(4)])
  def __lt__(self, rhs):
    return int(self) < int(rhs)
  def __str__(self):
    return '{' + ', '.join(['{1}:{0}'.format(self.coins[i], (1, 2, 5, 10)[i]) for i in range(4)]) + '}'
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)