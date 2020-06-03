def exploded(in_str):
    lst = []
    for i in in_str:
        lst.append(i)
    return lst

a=str(input("Provide input string "))
l=exploded(a)
print(l)