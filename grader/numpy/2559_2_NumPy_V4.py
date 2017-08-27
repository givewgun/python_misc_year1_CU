import numpy as np

def read_square_matrix():
    d = [int(e) for e in input().split()]
    m = [d]
    for k in range(len(d)-1):
        m.append([int(e) for e in input().split()])
    return np.array(m)
'''
array([[1, 1, 1, 1],
       [2, 2, 2, 2],
       [4, 4, 3, 3],
       [0, 0, 5, 5]])
'''
def min_in_each_row(m):
    return np.min(m,axis = 1) # หาวิธีเขียนแค่ค าสั่งเดียว
 
def max_in_each_column(m):#column
    return np.max(m,axis = 0) # หาวิธีเขียนแค่ค าสั่งเดียว
 
def diff_of_sums_of_two_diags(m):
     # หาวิธีเขียนอย่างมากสองค าสั่ง
    d1 = np.diag(m);d2 = np.diag(np.fliplr(m))
    return abs(np.sum(d1) - np.sum(d2))
'''ผลต่างระหว่างผลรวมของค่าในแนวทแยงมุมสองแนวของ
    m เช่น จากตัวอย่าง input ที่แสดงข้างบนนี้จะได้ผลคือ
    4
'''
 
def halve(m):

    n = int(m.shape[1]/2) # หาวิธีเขียนอย่างมากสองค าสั่ง

    
    b = np.array([ [ [m[2*i][2*j],m[2*i+1,2*j],m[2*i,2*j+1],m[2*i+1][2*j+1]] for j in range(n) ] for i in range(n) ])
    return np.sum(b,axis = 2)
 
exec(input().strip()) # do not remove this line
