tdic = dict()
def tiling(x, c):
    if x == 1: return 1
    if (x,c) in tdic:
        return  tdic[(x,c)]
    if c=="G":
        ans = tiling(x-1,'R')+tiling(x-1,'B')
        tdic[(x,c)]=ans
        return ans
    else:
        ans = tiling(x-1,'R')+tiling(x-1,'G')+tiling(x-1,'B')
        tdic[(x,c)]=ans
        return ans

N = int(input())
print(tiling(N,'G')+tiling(N,'R')+tiling(N,'B'))
