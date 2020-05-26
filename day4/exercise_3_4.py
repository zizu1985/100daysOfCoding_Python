lst=(input("Please enter a list of numbers : ")).split(" ")

# Accumualator pattern
lst100 = []
for l in lst:
    if 0 <= float(l) <= 100:
        lst100.append(l)

out=""
for i in lst100:
    out += str(i) + " "

print("The number between 0 and 100 are: " + out)
