import sys

a = float(input("Please take value for a "))
b = float(input("Please take value for b "))
c = float(input("Please take value for c "))
msg = "It is not perfect triangle"

check_triangle = (c ** 2) / ((a ** 2) + (b ** 2))

if check_triangle < 0.999 or check_triangle > 1.001:
    print("This is not a triangle")
    sys.exit(1)

a_check = a % 3
b_check = b % 4
c_check = c % 5
a_is_ok = False
b_is_ok = False
c_is_ok = False

if a_check <= 0.001:
    a_is_ok = True

if b_check <= 0.001:
    b_is_ok = True

if c_check <= 0.001:
    c_is_ok = True

if a_is_ok and b_is_ok and c_is_ok:
    msg = "It is perfect triangle"

print(msg)