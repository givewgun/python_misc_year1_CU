#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print("Welcome to Tower of Hanoi")
step = 0

def movetower(height,frompole,topole,withpole): 
    if height>1:
       global step
       movetower(height-1,frompole,withpole,topole)#1-2-3 . . -> 3 1-2 .
       step+=1  
       print("moving disk from ",frompole,"to pole",topole)#1-2-3 -> . 1-2 3
       step+=1
       movetower(height-1,withpole,topole,frompole)

       
def runtower(height,frompole,topole,withpole):
    global step
    movetower(height,frompole,topole,withpole)
    print("steps = ", step+1) #+1คือย้ายtowerกลับไปตอนสุดท้าน(ปิดจ๊อบ) . . 1-2-3
    
    
height,frompole,topole,withpole = input("Tower height,pole1,pole2,pole3 \n").split(",")

runtower(int(height),frompole,topole,withpole)
  

