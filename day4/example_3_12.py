filename = input("Please enter the name of a file:")
catfile = open(filename,"r")
for line in catfile:
    print(line)
catfile.close()

