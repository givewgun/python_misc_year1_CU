def same_row(i,j): # i และ j คือ index ในสตริง 81 ตัวที่แทนตาราง 9x9
    return (i//9 == j//9)
def same_col(i,j):
    return (i-j) % 9 == 0
def same_block(i,j):
    return (i//27 == j//27 and i%9//3 == j%9//3)
def show(board):
    for i in range(3):
        print('+---+---+---+')
        for j in range(3):
            k = 9*(3*i+j)
            print('|'+board[k:k+3]+'|'+board[k+3:k+6]+'|'+board[k+6:k+9]+'|')
    print('+---+---+---+')

def solve(board):
    #print("--------------")
    # หาซิว่า board ยังมี จุด เหลืออยู่ไหม ถ้าไม่มี ก็แสดง board และคืน board กลับไป
    if board.find(".") == -1:
        return board
    # แต่ถ้ายังมี จุด อยู่ใน board
    # สร้างเซต S ซึ่งเก็บตัวเลขที่อยู่ในแถวแนวนอนเดียวกับจุด ตัวเลขที่อยู่ในแถวแนวตั งเดียวกับจุด และตัวเลขที่อยู่ในกลุ่มเดียวกับจุด
    # (ท้าง่าย ๆ ด้วยการลุยทุกตัวใน board แล้วใช้ฟังก์ชัน same_row, same_col, same_block ให้เป็นประโยชน์)
    dot_i = board.find(".")
    #print("###################")
    #print(dot_i)
    #print("###################")
    S = set()
    for j in range(len(board)):
        if board[j] in "0123456789":
            if same_row(dot_i,j): S.add(board[j])
            if same_col(dot_i,j): S.add(board[j])
            if same_block(dot_i,j): S.add(board[j])
    #print(S)
    #print("###################")
    # ให้ T = เซตของเลข '0' ถึง '9' ลบด้วยเซต S (T ก็คือเซตที่เก็บเลขที่อาจใช้แทนจุดได้)
    T = set([str(e) for e in range(1,10)]) - S
    #print(T)
    #print("###################")
    for e in T:
        newboard = board[:dot_i] + e + board[dot_i+1:]#board ที่แทนจุดด้วย e
        #print(newboard)
        sol = solve(newboard) # จ้านวนจุดลดลงหนึ่ง ลองลุยหาค้าตอบต่อ
        if sol != '' : return sol # ถ้าลองแล้วใช้ได้ ก็คืนผล
    return '' # ถ้าลองทุกแบบ แล้วไม่ส้าเร็จ ก็คืน '' บอกว่าไม่พบค้าตอบ
sol = solve(input().strip())
show(sol)
