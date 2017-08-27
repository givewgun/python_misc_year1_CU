n = int(input().strip())
for i in range(n//2,0,-1):
 i -= 1
 print("."*(i)+"#"*(n-2*i)+"."*(i)+"."+"."*(i)+"#"*(n-2*i)+"."*(i))
for j in range((n//2-2)+1):
 print("#"*n+"#"+"#"*n)
for k in range(1,n+1):
 print("."*k + "#"*(n-k) + "#" + "#"*(n-k) + "."*k)
