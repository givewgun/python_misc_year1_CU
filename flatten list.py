#Flatten list
def flatten_list(d):
    flat = []
    for e in d:
        if type(e) is list:
            flat += flatten_list(e)
        else:
            flat.append(e)
    return flat

x = [1,[[[2,3],4]],[5,[6]],7,8]
print(flatten_list(x))
