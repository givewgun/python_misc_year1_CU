s = input().strip()
sn = ""
# if we want to remove a char/replace a char in that sring
#use .replace(unwanted,wanted)
#eg "123 456".replace(" ","") == "123456
#but we will use basic method instead
for char in s:
    if char != " ":
        sn += char
if sn.lower() == sn.lower()[::-1]:
    print('yes')
else:
    print('no')
# อีกแบบ------------------------------ 
state = True
for c in range(len(sn)//2):#use len // 2 because like flipping [Abc]Ba [aBc]bA  len//2 = 2 (012)
    if sn.lower()[c] != sn.lower()[(-c)-1]:
        state = False
        break
if state == True:
    print('yes')
else:
    print('no')
