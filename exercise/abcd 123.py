#Input string is in the set {A,B,C,D,E,F,G,H} and the corresponding value
#of each characteris the set {1,2,3,4,5,6,7,8}.
#Write a program that accepts the input string and change each
#character to its value then output the sum of all values.
inp = input('charr in the set {A,B,C,D,E,F,G,H} : ')
alp = 'ABCDEFGH'
num = '12345678'
value = 0
for c in inp:
    if c in alp:
        index_c = alp.find(c)
        value += int(num[index_c])
print(value)
        
