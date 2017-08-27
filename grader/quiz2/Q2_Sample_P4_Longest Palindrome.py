s = input().strip()
max_length = 0
min_pa = ""
for i in range(len(s)):
    for j in range(i,len(s)):
        sec = s[i:j+1]#according to suggestion from the paper
        if sec == sec[::-1]:
            pa = sec
            if len(pa) > max_length:
                max_length = len(pa)
                min_pa = pa
            elif len(pa) == max_length:
                if pa < min_pa:# because the sonner alphabet, the lower
                    max_length = len(pa)
                    min_pa = pa
print(min_pa)
                
            
        
