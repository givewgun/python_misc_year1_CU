class rint :
    def __init__(self, r):# r = str 123 -> str 321
        i = len(r) -1
        out = ""
        while i >= 0:
            out+= r[i]
            i -= 1
        self.r = out

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        out = ""
        for c in str(int(self)):
            out = c + out
        return out
    
    def __int__(self):
        return int(self.r)

    def __add__(self, rhs):
        return int(self)+int(rhs)

t, r1, r2 = input().split()
a = rint(r1); b = rint(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
