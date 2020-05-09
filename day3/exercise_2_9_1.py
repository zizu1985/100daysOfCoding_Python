x = float(input (" Please enter a number :"))
y = float (input (" Please enter a second number :"))
print("1) Add the two numbers ")
print("2) Subtract the two numbers ")
print("3) Multiply the two numbers ")
print("4) Divide the two numbers ")
choice = int(input (" Please enter your choice :"))
print("The answer is:", end="")

if choice == 1:
    print (x + y)
elif choice == 2:
    print (x - y)
elif choice == 3:
    print (x * y)
elif choice == 4:
    print (x / y)
else:
    print ("You did not enter a valid choice .")