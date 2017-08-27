s = input().strip()
storage = [] # for storing index of both 1char only and the second char
ns = "" #for checking wether we have that index of that char yet? (not in the desire order because it just a checker!!!
#ex Mississippi
for c in s:
    f_po = s.find(c)
    s2 = s[f_po+1:]
    sec_po = s2.find(c) #to see if there is the second char of that char or not
    if sec_po == -1:
        storage.append(f_po)
        ns += s[f_po]
    else:
        if s2[sec_po] not in ns:#                       s1  0 1234<-
            storage.append(sec_po + (f_po+1)) #because like A~BCDAE we want the second A, it is ABCDAE[(0+1)+3]
            ns += s2[sec_po]#                           s2    0123<-                
for d in sorted(storage):
    print(s[d],end ="")
# process https://goo.gl/P1QC22

