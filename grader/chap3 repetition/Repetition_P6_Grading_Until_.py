data = float(input())
grade = ""
while data >= 0:
    if data > 100:
        grade += "Error" + "\n"
        data = float(input())
    else:
        if 80<=data<=100:grade += 'A' +'\n'
        elif 75<=data<=79:grade += 'B+' +'\n'
        elif 70<=data<=74:grade += 'B' +'\n'
        elif 65<=data<=69:grade += 'C+' +'\n'
        elif 60<=data<=64:grade += 'C' +'\n'
        elif 55<=data<=59:grade += 'D+' +'\n'
        elif 50<=data<=54:grade += 'D' +'\n'
        else:grade += 'F' +'\n'
        data = float(input())
print(grade)
