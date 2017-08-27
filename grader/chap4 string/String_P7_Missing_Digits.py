n = input()
num = "0123456789"
state = [0,0,0,0,0,0,0,0,0,0]
miss = ""
for char in n:
    if char in num:
        state[int(char)] += 1
for i in range(len(state)):
    if state[i] == 0:
        miss += str(i) + " "
if len(miss) == 0:
    print('No missing digits')
else:
    print(miss)
