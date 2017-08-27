def function1():
    sum = 0
    for i in range(10):
        sum += i
    return sum
def function2(n):
    i = 2
    if n == 1:
        return False
    while i <= n**0.5:
        if n%i == 0:
            return False
        i += 1
    return True
def function3(n):
    for i in range(1,n):
        if function2(i):
            print(i)
def function4(x,y):
    match = 0
    notmatch = ''
    for i in x:
        if i == y:
            match += 1
        else:
            notmatch += i
    return [match,notmatch]
def main():
    f = input().strip()
    if f == "function1":
        print(function1())
    else:
        n = input().strip().split()
        if f == "function2":
            print(function2(int(n[0])))
        elif f == "function3":
            function3(int(n[0]))#เพราะในfมีprintอยู่บะ
        elif f == "function4":
            print(function4(n[0],n[1]))
main()
        
