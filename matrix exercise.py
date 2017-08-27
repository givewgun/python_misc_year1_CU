
def table():
    m = int(input('Number of rows: '))
    n = int(input('Number of column: '))
    x = []
    for i in range(m):
        x.append(input('row '+ str(i) + ';').split())
    for m in x:
        print(' '.join(m))
    print(x)

table()
