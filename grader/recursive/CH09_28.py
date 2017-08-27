def B_to_A( b ):
    if len(b)==1:
        return [b]
    if len(b)>=2:
        ret = []
        if type(b[0])!=list:
            ret = [[b[0]]+j for j in B_to_A(b[1])]

        else:
            for i in range(len(b)):
                ret+=B_to_A(b[i])

        return ret
        #if type(b[0])==list and type(b[1])==list:
            #return B_to_A(b[0])+B_to_A(b[1])
        #if type(b[0])!=list and type(b[1])==list:
            #return [[b[0]]+i for i in B_to_A(b[1])]
    
    

print(B_to_A(eval(input().strip()))) # do not remove this line
