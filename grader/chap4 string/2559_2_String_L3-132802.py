s1 = input().strip()
s2 = input().strip()
state = True
n1 = sorted("".join(s1.lower().split()))
n2 = sorted("".join(s2.lower().split()))
for i in range(len(n1)):
    if n1[i] != n2[i] or len(n1) != len(n2):
        state = False
        break
if state == False:
    print(s1,s2)
else:
    print(s1)

