#My magic number
import random
print('What is my magic number (1 to 100)')
mynumber  = random.randint(1,101)  #random() is (0,1) interval
ntries    = 1                     #or a = random.randint(1,100) is [1,99]
yourguess = -1
while ntries < 7 and yourguess != mynumber :
    msg = str(ntries) + '>> '
    if (ntries == 6) :
        print(msg + 'LAST CHANCE!')
    print(msg)
    yourguess = int(input('guess : '))
    if yourguess > mynumber :
        print('--> too high')
    elif yourguess < mynumber :
        print('--> too low')
    ntries += 1
if  yourguess == mynumber :
    print("Yes! It's my number")
else:
    print("Sorry! my number is",mynumber)
