def isSet(c1,c2,c3):
 # write your code here
 # 1จะเช็คcardเป็นัวๆ เช่น [purple,2 ,squiggle ,striped]
 #ทัละตัวทำเป็นsetละมาunionกับอีกสองไพ่ ภ้าเหมือนหมดlen = 1 ต่างหมด len = 3
 #ดังนั้นFalseเมื่อlen union = 2
    state = True
    for i in range(4):
        union = {c1[i]}.union({c2[i]}).union({c3[i]})
        if len(union) == 2:
            state = False
            break
    return state

cards = []
for i in range(12):
    cards.append(input().strip().split())
for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            if isSet(cards[i],cards[j],cards[k]):
                print(i,j,k)
