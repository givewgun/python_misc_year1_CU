s = input().strip()
s2 = ""
t = 0
for c in s:
    if c == "-":
        s2 += " " + "-"
    elif c == "+":
        s2 += " " + "+"
    else:
        s2 += c
#split string into list of str(integer)
for i in s2.split():
    t += int(i)
print(t)
t = 0
# another way of writing for in one line
t = sum([int(i) for i in s2.split()]) 
print(t)
