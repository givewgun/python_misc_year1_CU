#function exercise
num = input('Numbers :').split()
num = list(map(float,num))#เปลี่ยนเป็นfloatไม่งั้นเวลาเปรียบอาจมีผิดได้
print(num)
new=[]
def find_max(l): #find max
    return max(l)

def sort(l):
    if len(l) == 0:
        return new
    else:
        new.append(find_max(l))
        l.remove(find_max(l))
        sort(l)
    return new

def sort_reverse(l):
    return sort(l)[::-1]



print(find_max(num))
print(sort(num))
print(sort_reverse(num))


    
    
    
