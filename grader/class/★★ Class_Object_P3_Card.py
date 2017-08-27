class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit
  def __str__(self):
    return '({} {})'.format(self.value, self.suit)
  def getScore(self):
    if self.value == 'A': return 1
    if self.value in 'JQK': return 10
    return int(self.value)
  def sum(self, other):
    return (self.getScore() + other.getScore()) % 10
  def __lt__(self, rhs):
    v = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    s = ['club', 'diamond', 'heart', 'spade']
    if v.index(self.value) < v.index(rhs.value): return True
    if v.index(self.value) > v.index(rhs.value): return False
    if s.index(self.suit) < s.index(rhs.suit): return True
    return False
    
n = int(input())
cards = []
for i in range(n):
  value, suit = input().split()
  cards.append(Card(value, suit))
for i in range(n):
  print(cards[i].getScore())
print("----------")
for i in range(n-1):
  print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
  print(cards[i])