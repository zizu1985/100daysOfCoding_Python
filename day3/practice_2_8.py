try:
    age=int(input("How old you are?"))
except ValueError:
    print("You did not enter your age correctly")
    exit(0)

license=input("Do you have valid license?")
parlicense=input("Your parent has valid license?")

if (age <= 15 and parlicense == 'Yes') or (age > 16 and license == 'Yes'):
    print("You could legally fish in Minnesota")
else:
    print("You could not legally fish in Minnesota")

