sideA = float(input("Please enter the sideA of right triangle"))
sideB = float(input("Please enter the sideB of right triangle"))
sideC = round((sideA ** 2 + sideB ** 2) ** 0.5 , 3)
print("Hypotheneus of right for triangle with sides " + str(sideA) + " and " + str(sideB) + " equals " + str(sideC))