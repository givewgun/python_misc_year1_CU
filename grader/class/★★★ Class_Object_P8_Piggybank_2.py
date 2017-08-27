class piggybank:
  def __init__(self):
    self.coins = {}
  def add(self, v, n):
    if sum(self.coins.values()) + n > 100:
      return False
    v = float(v)
    if v not in self.coins:
      self.coins[v] = 0
    self.coins[v] += n
    return True
  def __float__(self):
    return float(sum([v*n for v, n in self.coins.items()]))
  def __str__(self):
    return '{' + ', '.join([str(v)+':'+str(n) for v, n in sorted(self.coins.items())]) + '}'
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)