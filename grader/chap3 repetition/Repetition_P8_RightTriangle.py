peri = int(input())
maxc = 0 #we need to find maxmum c
c=1
#a+b>c and a+b+c = perimeter
while peri >2*c: 
    for a in range(1,c):
        b =  peri-(a+c)#only two loops is enoguh cuz it takes long tie to compile
        if (a+b+c == peri and a**2+b**2 == c**2) and c>maxc:
            maxc = c
    c+=1#Keep find until it meets the condition
print(maxc)
