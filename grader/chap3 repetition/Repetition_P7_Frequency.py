n,same =[ int(e) for e in input().split() ]
count = 0
for i in range(n):
  m = int(input())
  if m ==  same:
    count +=1
print(count)
