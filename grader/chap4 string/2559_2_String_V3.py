s = input().strip().lower()
w = input().strip().lower()
sn = ""
for char in s:
    if char in ".,'"+'"':
        sn += " "
    else:
        sn += char
#string.split('char') will split sting by that char into an array
#if blank will split the blank space
#ex "GGGGuGGG".split('u') == ['GGGG','GGG']
sn = sn.split()
state = False
for data in sn:
    if data == w:
        state = True
        break 
if state == True:
    print('Found')
else:
    print('Not Found')

