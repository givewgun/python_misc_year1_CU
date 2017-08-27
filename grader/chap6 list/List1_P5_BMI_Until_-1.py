data = input().strip()
list = []
while data != "-1":
    list.append(data.split())
    data = input().strip()
for d in list:
    h = int(d[1])/100
    w = int(d[0])
    print(w/h/h)
    
