filename = input().strip()
found_id = ""
f = open(filename,'r')
lines =  f.readlines()
for line in lines:
    if line[:10] not in found_id:
        found_id += line[:10]+" "
        print(line[:10])
f.close()