import math
w = float(input()) # kg
h = float(input()) # cm

mos = math.sqrt(w*h) / 60
haycock = 0.024265 * (w**0.5378) * (h**0.3964)
boyd = 0.0333 * (w**(0.6157-0.0188*math.log(w,10))) * (h**0.3)
print(mos)
print(haycock)
print(boyd)
