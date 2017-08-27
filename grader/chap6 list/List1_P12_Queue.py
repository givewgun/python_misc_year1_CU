que = list(input().strip())
t = int(input().strip())
for i in range(t):
    met = [e for e in input().strip().split()]
    if met[0] == "in":
        que.insert(int(met[2]),met[1])
        print("".join(que))
    if met[0] == "out":
        que.pop(int(met[1]))
        print("".join(que))
    if met[0] == "swap":
        i1 = int(met[1])
        i2 = int(met[2])
        que[i1],que[i2] = que[i2],que[i1]
        print("".join(que))
