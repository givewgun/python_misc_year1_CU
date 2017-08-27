s = input().strip()
start,end = [ int(e) for e in input().split() ]#index, end is we want that position too ,so the real end [start:end+1]
if start == 0:
    print(s[end:start:-1] + s[0] + s[end+1:]) #in [] cant be negative(like range) only integers
else:
    print( s[:start] + s[end:start-1:-1] + s[end+1:] )    
 #start-1 because it will cut after the start (like [1:3] == 1 2 [3:0:-1] == 3 2 1
#when we want to reverse(including list and range etc.) more_less_-(number of skipping)
