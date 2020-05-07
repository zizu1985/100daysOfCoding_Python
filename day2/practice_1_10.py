'''
Write a short program that computes the length of the
hypotenuse of a right triangle given the two legs as pictured in Fig. 1.23 on
p. 35. The program should use three variables, sideA, sideB, and sideC. The
Pythagorean theorem states that the sum of the squares of the two legs of
the triangle equals the square of the hypotenuse. Be sure to assign all three
variables their correct values and print the length of sideC at the end of the
program. HINT: Raising a value to the 1/2 power is the same thing as finding
the square root. Try values 6 and 8 for sideA and sideB
'''

sideA = float(input("Please enter the sideA of right triangle"))
sideB = float(input("Please enter the sideB of right triangle"))
sideC = round((sideA ** 2 + sideB ** 2) ** 0.5 , 3)
print("Hypotheneus of right for triangle with sides " + str(sideA) + " and " + str(sideB) + " equals " + str(sideC))
