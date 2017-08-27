num = input() #รหัสๅ2หลัก
body = 0
for i in range(len(num)):
    body += (13-i) * int(num[i]) #ตามสูตร ใช้แบบ digit in num num.index(digit)...
digit_13 = (11 - (body%11))%10
print(digit_13)
