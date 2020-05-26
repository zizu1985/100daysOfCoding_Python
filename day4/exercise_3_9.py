print("Enter a list of integers terminated by a -1.")
lst =[]
first=int(input("Please enter the first integer and press enter: "))
lst.append(first)
while True:
    next=int(input("Please enter another integer : "))
    if next == -1:
        break
    lst.append(next)

out = ""
for l in lst:
    out = out + str(l) + " "

print("The list of integers is %s" % out)