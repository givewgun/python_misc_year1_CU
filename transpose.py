#Transpose matrix
def transpose(m):
    nr = len(m) #row
    nc = len(m[0]) # column mtrax=[[1,2,3],[2,3,4],[7,8,9]] บลาๆ
    t = [ [0]*nc for k in range(nr)]
    for i in range(nr):
        for j in range(nc):
            t[j][i] = m[i][j]
    return t

m = []
for i in range(3):
    m.append(input('row '+ str(i) + ';').split()) # 1 5 7 -> [[1,5,7]]

f = [ [ float(m[i][j]) for j in range(len(m[i])) ] \
      for i in range(len(m))] #แต่ละrow '''#j คือcolumnในrowนั้นๆ'''

t = transpose(f)
print(t)
