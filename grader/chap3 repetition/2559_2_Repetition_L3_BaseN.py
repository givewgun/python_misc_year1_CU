n,b = [ int(e) for e in input().split() ]
if n < 0 or (b<2 or b>9) :
    print("Error: Cannot convert")
else:
    out = ""
    if n == 0:
        out += '0'
    else:
        while n > 0:
            if n % b != 0:
                out = str(n % b) + out # !!!when we add we need to add at the front not the end
            else:
                out = "0" + out
            n //= b 
    print(out)
