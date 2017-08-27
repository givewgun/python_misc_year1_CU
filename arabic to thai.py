#เปลี่ยนเลขอารบิกเป็นเลขไทย
s = input('type: ')
thai = ''
for d in s:
    k = '0123456789'.find(d) #k เป็นเลขindex
    if k >= 0:
        thai += '๐๑๒๓๔๕๖๗๘๙'[k]
    else:
        thai += d
print(thai)
        
        
