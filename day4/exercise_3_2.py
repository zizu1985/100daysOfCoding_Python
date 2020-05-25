phonebookname = "addressbook.txt"
# We assume phonebook is already created
phonebook = None
choice = 1

while choice != 3:
    print("1) Look up a person by last name")
    print("2) Add a person to the address book.")
    print("3) Quit")
    choice = int(input("Enter your choice:"))
    if choice == 2:

        if phonebook is None or phonebook.closed:
            phonebook = open(phonebookname,'a')

        writeList = []
        lastName = str(input("LastName: "))
        writeList.append(lastName + "\n")
        firstName = str(input("FirstName: "))
        writeList.append(firstName + "\n")
        street = str(input("Street:"))
        writeList.append(street + "\n")
        citystatezip = str(input("City State Zip:"))
        writeList.append(citystatezip + "\n")
        homephone = str(input("Homephone:"))
        writeList.append(homephone + "\n")
        mobilephone = str(input("MobilePhone: "))
        writeList.append(mobilephone + "\n")

        if len(writeList) > 0:
            phonebook.writelines(writeList)
        phonebook.close()

    if choice == 1:
        if phonebook is None or phonebook.closed:
            phonebook = open(phonebookname,'r')
        lastName = str(input("Please enter the last name "))
        lastNameFromFile = phonebook.readline().rstrip()
        while lastNameFromFile != "":
            firstName = phonebook.readline().rstrip()
            street = phonebook.readline().rstrip()
            citystatezip = phonebook.readline().rstrip()
            homephone = phonebook.readline().rstrip()
            mobilephone = phonebook.readline().rstrip()
            if lastNameFromFile == lastName:
                print(lastName)
                print(firstName)
                print(street)
                print(citystatezip)
                print(homephone)
                print(mobilephone)
                break;
            lastNameFromFile = phonebook.readline().rstrip()
        phonebook.close()

print("Done")
