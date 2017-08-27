t = input('t = ') #A12QAAB2
counts = {}
for c in t:
    if c in counts:      #เพราะไม่งั้นมันจะหาkeyไม่เจอเลย เพราะเริ่มต้นมันไม่มีห่าไรในดิกเลย
        counts[c] += 1
    else:
        counts[c] = 1
for c in sorted(counts.keys()): #ลำดับkeyที่จะหลุดมันจะไม่เรียง ต้งเรียงเอง sorted
    print(c, counts[c])
