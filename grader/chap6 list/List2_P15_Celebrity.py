d = int(input().strip())#= len(row) = len(col)
row = [[] for e in range(d)]
col = [[] for e in range(d)]
for i in range(d):
    data = [int(e) for e in input().strip().split()]
    row[i] = data
    for j in range(d):
        col[j].append(data[j])
#--------
#ถ้าpopแสดงว่า ในแถวรวม==1 ในcolรวม ==d
find = False
for k in range(d):#k คือ row และ col 1 1 2 2 3 3 4 4...
        if sum(row[k]) == 1 and sum(col[k]) == d:
            print(k)
            find = True
if find == False:
    print(-1)
