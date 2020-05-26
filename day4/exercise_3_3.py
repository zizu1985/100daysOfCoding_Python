lst=(input("Please enter a list of numbers : ")).split(" ")

# Accumualator pattern
count = 0
sum = 0
for l in lst:
    count += 1
    sum += float(l)

avg = round(sum / count,2)

print("There were %d numbers in the list" % count)
print("The average of numbers was %.2f" % avg)