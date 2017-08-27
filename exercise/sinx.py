import math
x = int(input('Angle in rad : '))
power = 1
sin_x = 0
while power < 5 :
    position = (-1) ** (power-1)
    new_power = 2*power - 1
    sin_x += position * (x **(new_power / math.factorial(new_power)))
    power +=1
    print(position, power, new_power, sin_x)
print('sin(x) = ',sin_x)
print(math.sin(x))
