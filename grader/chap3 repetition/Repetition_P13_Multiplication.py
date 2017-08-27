r,c = [int(e) for e in input().split()]
row = ""
for i in range(1,r+1):
    row = ""
    for j in range(1,c+1):
        row += str(i*j) + " "
    print(row)

    
        
