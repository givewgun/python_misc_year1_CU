l1 = [e for e in input().strip().split()]
l2 = [e for e in input().strip().split()]
word = [e for e in input().strip().split()]
out = ""
for i in range(len(word)):
    if word[i] in l1:
        out += l2[l1.index(word[i])] + " "
    elif word[i] in l2:
        out += l1[l2.index(word[i])] + " "
    else:
        out += word[i] + " "

print(out.strip())

        
