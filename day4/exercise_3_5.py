lst=(input("Please enter a list : ")).split(" ")
src = lst.copy()
rev=[]

while len(src) > 0:
    rev.append(src.pop())

out = ""
for l in lst:
    out = out + str(l) + " "
print(out)

out = ""
for r in rev:
    out = out + str(r) + " "

print(out)