#list total
def listsum(x):
    if len(x) == 1:
        return x[0]
    return x[0] + listsum(x[1:])

print(listsum([1,3,5,7,9]))

