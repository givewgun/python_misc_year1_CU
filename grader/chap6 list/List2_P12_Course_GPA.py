ns,nc = [int(e) for e in input().strip().split()]
g = ["A","B+","B","C+","C","D+","D","F"]
s = [4,3.5,3,2.5,2,1.5,1,0]
t = []
for i in range(ns):
    sum = 0
    count = 0
    grade = input().strip().split()
    for c in grade:
        if c != "X":
            index = g.index(c)
            sum += s[index]
            count += 1
    avg = sum / count
    t.append(avg)
for n in t:
    print("%.2f" % n)
