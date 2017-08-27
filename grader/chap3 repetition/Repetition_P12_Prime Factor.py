''' กาก
n = int(input())
fprime = ""
state = True
for i in range(2,n+1):
    state = True
    for j in range(2,i):
        if i%j == 0:
            state = False
    if n%i == 0 and state == True:
        fprime += str(i) + " "
print(fprime)
'''
#optimize
import time
start_time = time.time()

n = int(input())
fprime = ""

state = False #เช็คว่าจริงจะง่ายกว่า ๖ได้เป็นตัวๆ ปึ้บๆเลย)
for i in range(2,n+1):
    if n%i == 0: #เช็คก่อนว่าหารลงไหม จะช่วยลดได้เยอะ
        state = True
        for j in range(2,i):
            if i%j == 0:
                state = False
        if state == True:
            fprime += str(i) + " "
#while is somewhat slower
'''
state = False
for i in range(2,n+1):
    if n%i ==0:
        j = 2
        state = True
        while j<i and state == True: #keep finding number one-by-one
            if i%j == 0:
                state = False
            j += 1
        if state == True:
            fprime += str(i) + " "
'''
    

print(fprime)

print("--- %s seconds ---" % (time.time() - start_time)) #I copy this code from the internet
#please don't ask. I just use it to check the run time
