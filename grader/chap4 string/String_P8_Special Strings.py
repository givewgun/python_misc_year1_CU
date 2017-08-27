s = input().strip()
sl = s.lower() # a < b because much like index 0<1 x<y but a>A
state  = True
for i in range(len(sl)-1):
    if sl[i] > sl[i+1]:
        state = False
if state == False:
    print("no")
else:
    print("yes")
