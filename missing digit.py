#missing digit
digits = input('Enters ten digits : ')

while type(digits) != int and len(digits.strip()) != 10:
    print("It's not a ten digits number you dumb fuck")
    digits = input('Enters ten digits : ')


counts = [False]*10
for num in digits:
    for x in range(10):
        if str(x) in digits:
            counts[x] = True

if counts.count(False) == 0:
    print('No missing digit')
elif counts.count(False) == 1:
    print("Missing digit is ", counts.index(False))
elif counts.count(False) > 1:
    missing = [ k for k in range(10) if counts[k] == False ]
    print('Missing numbers are', ' '.join(map(str , missing)))


'''
    missing = ''
    for k in range(10):
        if counts[k] == False:
            missing += str(k) + ' '
    print('Missing numbers are', missing)
'''
