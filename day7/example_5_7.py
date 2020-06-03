def reverse(s):
    result = ""
    for c in s:
        result = c + result
    return result

t = input("Please enter a string:")
while t.strip() != "":
    print("The reverse of",t,"is",reverse(t))
    t = input("Enter another string or press enter to quit: ")
