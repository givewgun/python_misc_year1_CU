#anagram
def anagram1(x) :
    if len(x) <= 1:
        return {x}
    result = set()
    for i in range(len(x)):
        for a in anagram1(x[:i]+x[i+1:]):
            result.add(x[i]+a)
    return result


#แบบset comprehension
def anagram2(y):
    if len(y) <= 1:
        return {y}
    return { y[i]+a for i in range(len(y))
             for a in anagram2(y[:i]+y[i+1:]) }



print(anagram1('muslim'))
print(anagram2('man'))
