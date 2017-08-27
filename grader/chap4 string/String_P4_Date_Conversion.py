m,d,y = [ str(e) for e in input().split('/') ]
month = "JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC"
#        0  3  6  9  12 15 18 21 27 27 ....
#        1  2  3  4  5  6  7  8  9  10  
m_start = 3*(int(m)-1)
print(d,month[m_start:m_start+3],y)
