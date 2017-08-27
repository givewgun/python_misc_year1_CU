#traditional unorthodox
s = input().strip()
sn = ""
num = "0123456789"
w1 = "zottffssen"
w2 = "enwhoiieii"
w3 = "reoruvxvgn"
w4 = "o  ere ehe"
w5 = "   e   nt "
for c in s:
    n = ""
    if c in num:
        n += w1[int(c)]+w2[int(c)]+w3[int(c)]+w4[int(c)]+w5[int(c)]
        n = "".join(n.split()) #join array into string with blank interval ex( "!".join("kuy gun".split()) == "kuy!gun"
        sn += n + " "
    else:
        if (c == "-" or c == " ") and sn[-1] == " ": #ex s= K 123-456 sn =K one two three -four five six ; we must remove one space infront of -
            sn = sn[:-1] + c #ex Circle 4 cm. -> Circle four  cm. (1 excess " ")
        else:
            sn += c
print(sn)
#array (list)-------------------------------
w = ['zero','one','two','three','four','five','six','seven','eight','nine']
sn2 = ""
for c in s:
    if c in "0123456789":
        sn2 += w[int(c)] + " "
    else:
        if (c == "-" or c == " ") and sn2[-1] == " ": #ex s= K 123-456 sn =K one two three -four five six ; we must remove one space infront of -
            sn2 = sn2[:-1] + c #ex Circle 4 cm. -> Circle four  cm. (1 excess " ")
        else:
            sn2+= c
print(sn2)
