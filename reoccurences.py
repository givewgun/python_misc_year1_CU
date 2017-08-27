#reoccurences
string=input('plz input ')
reoccur_str =''
for i in string:
    if string.count(i) > 1:
        if i not in reoccur_str: reoccur_str += i

print(reoccur_str)
    
        
    
