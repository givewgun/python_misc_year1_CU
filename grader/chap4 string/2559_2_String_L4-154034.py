'''
m = input().strip()
s = input().strip()
re = input().strip()
rep = input().strip()
if m == "R":
    print(s[:s.lower().find(re.lower())] + rep + s[s.lower().find(re.lower())+ len(re):])
else:
    print(s.replace(re.lower(),rep))
'''
mode = input().strip()
word = input().strip()
wordL = word.lower()
wordA = input().strip()
wordAL = wordA.lower()
wordB = input().strip()
wordNew = ""
s = wordL.find(wordAL)
while s >= 0 :
    wordNew += word[:s] + wordB
    word = word[s + len(wordA):]
    if mode == "R" :
        break
    s = word.lower().find(wordAL)
print(wordNew + word)
