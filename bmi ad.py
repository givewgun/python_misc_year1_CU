#BMI ADVANCE
import math
w = float(input('Weight (kg.) : '))
if w <= 10:
    print('นน.เบาไป')
    exit(1)
h = float(input('height (cm.) : '))
if h ==0:
    print('impossible')
    exit(1)
bsa = 3.207e-4 * h**0.3 * (1000*w)**(0.7285-0.0188*(3+math.log(w,10)))#log(x,base)                                                                    
print('BMI =', bsa)                                                   #and Ae... = A* 10**
