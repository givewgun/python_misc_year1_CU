file1 = open("file1.txt","r")
a = set()#
for line in file1:
    s = ""
    for c in line.strip():
        if c.lower() in "abcdefghijklmnopqrstuvwxyz":
            s += c.lower()
        else:
            s += ' '
    line = s.split()
    a.update(line)

file2 = open("file2.txt","r")
b = set()
for line in file2:
    s = ""
    for c in line.strip():
        if c.lower() in "abcdefghijklmnopqrstuvwxyz":
            s += c.lower()
        else:
            s += ' '
    line = s.split()
    b.update(line)

word = input().strip().lower()
if word in a and word in b:
    print("Found in both files")
elif word in a and word not in b:
    print("Found in file1 only")
elif word not in a and word in b:
    print("Found in file2 only")
else:
    print("Not found")
