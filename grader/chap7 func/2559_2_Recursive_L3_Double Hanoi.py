def dhanoi(n,left,mid,right):
    if n == 0 : return
    dhanoi(n-1,left,mid,right)#   เริ่มดวยท า Double Hanoi เพื่อยายจาน 1B,1W ถึง (n-1)B,(n-1)W จากเสาซาย ไป เสาขวา
    print(str(n)+'W',':',left,'->',mid) # ย้ายจาน หมายเลข nW จากเสาซ้ายไปกลาง 
    print(str(n)+'B',':',left,'->',mid)# ตามด้วยย้ายจาน หมายเลข nB จาก เสาซ้ายไปกลาง
    dhanoi(n-1,right,mid,left)# ท า Double Hanoi เพื่อยายจาน 1B,1W ถึง (n-1)B,(n-1)W จากเสาขวา กลับมา เสาซาย
    print(str(n)+'B',':',mid,'->',right)# (n-1)B,(n-1)W จากเสาขวา กลับมา เสาซาย
    print(str(n)+'W',':',mid,'->',right)# 
    dhanoi(n-1,left,mid,right)
exec(input().strip()) # don't remove this line
