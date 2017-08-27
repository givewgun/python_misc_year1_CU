rock = [int(e) for e in input().strip().split()]
print(rock)
score1 = 0
score2 = 0
for i in range(len(rock)):
    if i%2 == 0:# player1 round
        score1 += max(rock[0],rock[-1])
        rock.remove(max(rock[0],rock[-1]))
    else:
        score2 += max(rock[0],rock[-1])
        rock.remove(max(rock[0],rock[-1]))
print(score1)
print(score2)
if score1 > score2:
    print(1)
elif score1 < score2:
    print(2)
else:
    print(0)
