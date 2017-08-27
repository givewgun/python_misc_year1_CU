file = open("address.txt", "r")
addr = dict()
for line in file:
    data = line.strip().split()
    addr[(data[0],data[1])] = data[2],data[3]
file.close()

while True :
    search = input().strip()
    if search == "" :
        break
    name, surname = search.split()
    if (name, surname) in addr.keys() :
        print(" ".join(addr[(name, surname)]))
    else :
        print("Not found")

