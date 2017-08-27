def remove_symbol(s):
  symbol = '0123456789+-,./!'
  s2 = ''
  for c in s:
    if c in symbol: s2 += ' '
    else:           s2 += c.lower()
  return s2

def str_to_unique_list(s):
  L = []
  for w in s.split():
    if w not in L:
      L.append(w)
  return L

def percent_in_list(template, test):
  c = 0
  for i in test:
    if i in template:
      c += 1
  return c*100/len(test)

def main():
  good = input().strip()
  good_list = str_to_unique_list(remove_symbol(good))

  bad = input().strip()
  bad_list = str_to_unique_list(remove_symbol(bad))

  n = int(input())
  for i in range(n):
    test = input().strip()
    test_list = str_to_unique_list(remove_symbol(test))
    
    good_p = percent_in_list(good_list,test_list)
    bad_p  = percent_in_list(bad_list,test_list)

    print(test_list)
    print(good_p, bad_p)

exec(input().strip())
# do not remove this line