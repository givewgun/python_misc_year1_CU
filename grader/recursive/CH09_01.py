def fact(k):
    if k==0 or k==1:
        return 1
    return k*fact(k-1)
print(fact(int(input())))
