#Input string is in the set                      {A,B,C,D,E,F,G,H}\
# and the corresponding output string is the set {X,Y,Z,I,J,K,L,M}
inp = input('string : ').strip()
new_text = ''
original = 'ABCDEFGH'
original_low = original.lower()
new      = 'XYZIJKLM'
new_low = new.lower()
for c in inp:
    if c in original:
        index_c = original.find(c.upper())
        new_text += new[index_c]
    if c in original_low :
        index_c = original_low.find(c.lower())
        new_text += new_low[index_c]
    elif c not in original and original_low:
        new_text +=c
print(new_text)
    
    
        
