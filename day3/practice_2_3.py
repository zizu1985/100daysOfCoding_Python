import sys

a = int(input("Please take value for a "))
b = int(input("Please take value for b "))
c = int(input("Please take value for c "))
msg = "It is a perfect triangle"

if (c ** 2) != ((a ** 2) + (b ** 2)):
    print("This is not a triangle")
    sys.exit(1)

if a % 3 != 0 or b % 4 != 0 or c % 5 != 0:
    msg = "It is not perfect triangle"

print(msg)