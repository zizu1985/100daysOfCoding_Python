'''
Write a program that capitalizes the first four
characters of a string by converting
the characters to their ASCII equivalent, then adding the necessary amount to capitalize them,
and converting the integers back to characters. Print the capitalized
string. Here is a sample of running this program.

Please enter a four character string : kent
The string capitalized i s KENT
'''

name=input("Please enter a four character string: ")

s_ASCII = ord('s')
S_ASCII = ord('S')
diff = abs(s_ASCII - S_ASCII)

out = ''
for n in name:
    s = ord(n)
    large_int = s - diff
    out += chr(large_int)

print('The string capitalized is %s' % (out))
