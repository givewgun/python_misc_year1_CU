n = int(input())
state = False
for x in range(n):
    for y in range(x,n):
        if x**2 + y**2 == n:
            print(x, y)
            state = True
if state == False:
    print('No solution')
