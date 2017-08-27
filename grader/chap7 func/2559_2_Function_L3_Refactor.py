def extract_sign(t):
    sign = ''
    if t[0]=='-':
        t = t[1:]
        sign = 'lop-'
    return sign,t
def split_by_point(t):
    k = t.find('.')
    d = ''
    if k >= 0:
        d = t[k+1:]
        t = t[:k]
    return t,d
def remove_comma(t):
    return t.replace(',' , '')
def split_by_million(t):
    tm = ''
    if len(t) > 6 :
        tm = t[:-6]
        t = t[-6:]
    return tm,t
def digit_to_text(d):
    digits = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
    return digits[d*5:d*5+5].strip()
def pos_to_text(p):
    pos = '    sip roeypun muensaenlarn'
    return pos[p*4:p*4+4].strip()
def right_of_jood_to_text(t):
    out = ''
    for d in t:
        out += '-' + digit_to_text(int(d))
    return out
def number_to_text(t):
    t1 = ''
    for p in range(len(t)):
        c = t[len(t)-p-1]
        if c == '0' : continue
        k = int(c)
        tmp = digit_to_text(k) + '-' + pos_to_text(p)
        #print(tmp)
        if p == 0 :
            t1 = tmp
        else:
            t1 = tmp + '-' + t1
    t1 = t1[:-1]
    if t1[-5:] == '-soon' : t1 = t1[:-5]
    t1 = t1.replace('song-sip', 'yee-sip')
    t1 = t1.replace('nueng-sip', 'sip')
    t1 = t1.replace('sip-nueng', 'sip-ed')
    return t1
def combine(moreM, lessM):
    out = lessM
    if moreM == '' and lessM == '' : out = 'soon'
    elif moreM != '' and lessM == '' : out = moreM + '-larn'
    elif moreM != '' and lessM != '' : out = moreM + '-larn-' + lessM
    return out
def main():
    num = input().strip()
    sign,num = extract_sign(num)
    #print(sign,num)
    #print("----")
    leftJ,rightJ = split_by_point(num)
    #print(leftJ,rightJ)
    #print("----")
    leftJ = remove_comma(leftJ)
    #print(leftJ)
    #print("----")
    moreM,lessM = split_by_million(leftJ)
    #print(moreM,lessM)
    #print("----")
    tLessM = number_to_text(lessM)
    tMoreM = number_to_text(moreM)
    out = combine(tMoreM, tLessM)
    if rightJ != '' :
        out += '-jood'
    for d in rightJ:
        out += '-' + digit_to_text(int(d))
    
    print(sign + out)
    
exec(input().strip())

