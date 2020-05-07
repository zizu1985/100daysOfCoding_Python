'''

Write the three line program given in the two listings on p. 24.
Then, without writing the string literal “house”, modify it to print the string
“house” to the screen using string indexing. HINT: You can add strings together
to build a new string. So,
name = " Sophus " + "Lie"
will result in name referring to the string “Sophus Lie

'''
name = 'Sophus Lie'
house = name[3] + name[1] + name[4] + name[5] + name[9]
print("House is ", house)

