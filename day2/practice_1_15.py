'''
Practice 1.15 Re-do Practice Problem 1.14 using format specifiers when
printing instead of converting each item to a string. The goal is for the output
to look exactly the same.
sum (1..100)
'''
one = 1
hun = 100

sum = hun * ((hun + 1)/2)
print("sum(%d..%d)=%d"%(one,hun,sum))