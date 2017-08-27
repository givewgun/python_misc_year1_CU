#convert month into number
month = input('Month?:').strip()
#       012345678901234567890123456789012345
abbr = 'JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC'
k = abbr.find(month[0:3].upper())
print(k)
if k <= 0 : #ถ้า ไม่มีstring find ยังไงก็=0
    print('Invalid month abberviation')
else:
    print(month, '-->' , 1+k//3)
    print(month.upper(),' abbr: ', abbr[k:k+3])
