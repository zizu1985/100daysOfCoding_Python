def implode(lst):
    out=''
    for l in lst:
        out = out  + l
    return out

a=list(str(input("Provide input string ")))
print(type(a))
l=implode(a)
print(type(l))
print(l)