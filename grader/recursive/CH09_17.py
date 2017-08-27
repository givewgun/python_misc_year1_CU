def string2list(s):
 s = s.strip()
 if s == '[]':
     return []
 if s.find('[') < 0:
     return int(s)
 count = 0
 ans = []
 start = 1
 for i in range(1, len(s)-1):
     if s[i] == '[':
         count+=1
     elif s[i] == ']':
         count-=1
     elif s[i] == ',' and count == 0:
         ans.append(string2list(s[start:i]))
         start = i+1
 ans.append(string2list(s[start:len(s)-1]))
 return ans

def doublelist(mylist):
    ans = list()
    for i in mylist:
        if type(i)!=list:
            ans.append(i)
            ans.append(i)
        else:
            ans.append(doublelist(i))
            ans.append(doublelist(i))
    return ans
mylist = input().strip()
print(doublelist(string2list(mylist)))
