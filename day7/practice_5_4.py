def length(L):
    # object not callable
    l = 1
    for i in range(len(L)):
        l = l + 1
    return l

print(length([1,2,3]))

