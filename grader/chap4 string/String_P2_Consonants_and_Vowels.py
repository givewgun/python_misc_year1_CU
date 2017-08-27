s = input()
alpha = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"
ac = 0
vc = 0
for char in s:
    if char in alpha.upper() or char in alpha:
        ac += 1
    elif char in vowel.upper() or char in vowel:
        vc += 1
print(vc,ac)
