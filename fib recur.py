def fibo(n):
    if n == 1 or n==2:
        return 1
    else:
        num = fibo(n-1) + fibo(n-2)
        return num

def fibo_sum(n) :
    total = 0
    for i in range(1,n+1):
        total += fibo(i)
    return total

def sequence_fibo(n):
    sequence =""
    for i in range(1,n+1):
        sequence += (str(fibo(i))+" ")
    return sequence

def factorial(n):
    if n == 1:
        return 1
    else:
         return n * factorial(n-1)
def factorial_seq(n):
    seq = ""
    for i in range(0,n):
        if n-i == 1:
            seq += "1"
        else:
            seq += str(n-i) + "*"
    return seq
    
    
    
#Fib 3 = 1+1
#fib4 = 1+1+2
n = int(input())
print("Number at position " + str(n)+" = "+ str(fibo(n)) + '\n'\
      "Sum until position " + str(n)+" = "+ str(fibo_sum(n))+'\n'\
      "Sequence = "+ str(sequence_fibo(n)))
print("For factorial at position " + str(n) + '\n'\
      "Factorial product = " + str(factorial(n)) +'\n'\
      "Factorial sequence " + str(n) +"! = " + factorial_seq(n))
      

    
