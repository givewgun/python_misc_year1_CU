import timeit

start = timeit.default_timer()




n = int(input().strip())
l = []
no_recur = []
high =""
max = 0
for i in range(n):
    l.append(input().strip())
for c in l:
    if c not in no_recur:
       no_recur.append(c)
for c in no_recur:
    if l.count(c) > max:
        max = l.count(c)
        high = c
    elif l.count(c) == max and c < high:
        high = c
print(high)
stop = timeit.default_timer()

print(stop - start)
