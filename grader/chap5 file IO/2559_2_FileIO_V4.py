infile = open(input().strip(),'r')
w = [input().strip(),input().strip(),input().strip()]
n = ""
for l in infile:
    l = l.strip()
    for c in l:
        n += c
n = sorted(n)
c = [n.count(w[0]),n.count(w[1]),n.count(w[2])]
s = ""
for i in range(3):
        if i == 0:
            s += w[c.index(max(c))]
        elif i == 1:
            for d in c:
                if d != max(c) and d!= min(c):
                    s += w[c.index(d)]
        elif i == 2:
            s += w[c.index(min(c))]
print(s)
    
        
        
        
