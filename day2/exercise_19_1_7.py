'''
Please enter an eight digit binary number : 01010011
The decimal equivalent of 01010011 i s 83.
'''

number2 = input("Please enter an eight digit binary number :")
ret = 0
multi = 0

for digit in reversed(number2):
    if int(digit) == 1:
        ret += 2 ** multi
    multi += 1

print("The decimal equivalent of %s i s %d" % (number2,ret))
