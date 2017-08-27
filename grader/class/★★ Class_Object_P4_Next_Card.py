class Card:
  
  def __init__(self, value, suit):
    self.v = value
    self.s = suit
  
  def __str__(self):
    return '({} {})'.format(self.v, self.s)
    
  def next1(self):
    sl = 'club', 'diamond', 'heart', 'spade'
    vl = tuple('3456789') + ('10',) + tuple('JQKA2')
    ns = sl[(sl.index(self.s) + 1) % 4]
    nv = self.v
    if ns < self.s:
      nv = vl[(vl.index(self.v) + 1) % 13]
    return Card(nv, ns)
  
  def next2(self):
    nxt = self.next1()
    self.v = nxt.v
    self.s = nxt.s
    
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])