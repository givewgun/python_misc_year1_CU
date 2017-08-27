def make_int_list(x):
    l = [ int(i) for i in x.strip().split()]
    return l# รับสตริง x มาแยกและแปลงเปน int เก็บใน list แลวคืนเปนผลลัพธ
    # เชน x = '12 34 5' ไดผลเปน [12, 34, 5]
def is_odd(e):
    if e%2 != 0:
        return True
    else:
        return False# คืนคาจริงเมื่อ e เปนจํานวนคี่ ถาไมใช คืนคาเท็จ
def odd_list(alist):
    l = [i for i in alist if is_odd(i)]# คืน list ที่มีคาเหมือน alist แตมีเฉพาะตัวที่เปนจํานวนคี่
    return l# เชน alis = [10, 11, 13, 24, 25] จะได [11, 13, 25]
def sum_square(alist):
    t = 0
    for i in alist:
        t += i**2# คืนผลรวมของกําลังสองของแตละคาใน alist
    return t# เชน alist = [1,3,4] ไดผลเปน (1*1 + 3*3 + 4*4) = 26
exec(input().strip()) # ตองมีบรรทัดนี้เมื่อสงไป grader
