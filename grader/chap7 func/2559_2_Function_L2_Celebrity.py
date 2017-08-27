# R = {person:know}
def knows(R,x,y):
    if y in R[x]:
        return True
    return False
def is_celeb(R,x):
    if len(R[x]|{x}) != 1:
        return False
    R_c = dict(R)
    R_c.pop(x)
    #print(x)
    #print("---------")
    #print(R_c)
    #print("---------")
    for y in R_c:
        if not knows(R_c,y,x):#y knows x ?
            #print(y, "not knows", x)
            return False
    return True
def find_celeb(R):
    for x in R:
        if is_celeb(R,x):
            return x
    return None
def read_relations() :
    R = dict()
    while True:
        d = input().split()#Ploy Pat
        if len(d) == 1: break
        else:
            if d[0] not in R:
                R[d[0]] = set()
            if d[1] not in R:
                R[d[1]] = set()
            if d[0] != d[1]:
                R[d[0]].add(d[1])
    return R
def main():
    R = read_relations()
    #print(R)
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip())
