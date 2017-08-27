'''
fac(7) ได
สตริง '7!'
oneterm(2.4, 5) ได
สตริง '2.4**5/5!'
sin(8,6) ได
สตริง '8 - 8**3/3! + 8**5/5! - 8**7/7! + 8**9/9! - 8**11/11!'
sin(1.5,4) ได
สตริง '1.5 - 1.5**3/3! + 1.5**5/5! - 1.5**7/7!'

'''
def fac(n): # เชน n = 7 fac(n) ได'7!'
    return str(n)+"!"
def oneterm(x,n): # เชน x = 2, n = 3 oneterm(x,n) ได'2**3/3!'
    return str(x) + "**" + str(n) + "/" +fac(n)
def sin(x,n):# เชน x=2,n=3 sin(x,n) ได'2 - 2**3/3! + 2**5/5!'
    out = str(x)#out มีคาเป&นสตริงของคาใน x
    k = 3
    sign = "-"
    for i in range(n-1):#วงวนหมุน n-1 รอบ
        out = out + " " + sign + " " + oneterm(x,k)#นําผลของ ' ' ตอกับ sign ' ' ตอกับ oneterm(x,k) ไปตอเขาทางขวา out
        k += 2#เพิ่ม k อีก 2
        if sign == "-":
            sign = "+"
        elif sign == "+":
            sign = "-"#ถา sign เป&น ลบ เปลี่ยนเป&นบวก ถาเป&นบวก ก็เปลี่ยนเป&นลบ
    return(out)#คืน out เป&นผลที่ไดจากฟงกชัน sin
exec(input().strip()) # ตองมีบรรทัดนี้ในโปรแกรมตอนสงไป grader

