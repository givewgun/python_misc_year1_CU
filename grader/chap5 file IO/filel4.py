f = open(input().strip())
times = int(input().strip())
wordA = input().strip("\n\r")
wordB = input().strip("\n\r")
output = ""
count = 1
for line in f :
    lineN = line
    s = lineN.lower().find(wordA.lower())
    while s >= 0 and count <= times :
        count += 1
        output += lineN[:s] + wordB
        lineN = lineN[s + len(wordA):]
        s = lineN.lower().find(wordA.lower())
    if s == -1 or count > times :
        output += lineN
print(output)
f.close()