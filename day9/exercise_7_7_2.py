phonebookname = "addressbook.txt"
# We assume phonebook is already created
phonebook = None



# Store all addresscard
addresscards = []


class AddressCard:
    """
        Create new Address Card
    """

    def __init__(self, last, first, street, city, country, zip, phone, mobile):
        self.last = last
        self.first = first
        self.street = street
        self.city = city
        self.country = country
        self.zip = zip
        self.phone = phone
        self.mobile = mobile

    def getmobile(self):
        return self.mobile

    def getlast(self):
        return self.last

    def getphone(self):
        return self.phone

    def getzip(self):
        return self.zip

    def getcountry(self):
        return self.country

    def getcity(self):
        return self.city

    def getstreet(self):
        return self.street

    def getfirst(self):
        return self.first

    def __str__(self):
        return self.getfirst() + " " + self.getlast() + "\n" + \
               self.getstreet() + "\n" + \
               self.getcountry() + " , " + \
               self.getcity() + " " + self.getzip() + "\n" + \
               self.getphone() + "\n" + \
               self.getmobile() + "\n"

    def __eq__(self, other):
        if type(other) != type(self):
            raise Exception("Invalid Comparision")

        if self.last + "," + self.first == \
                other.last + "," + other.first:
            return True
        return False

    def __lt__(self, other):
        if type(other) != type(self):
            raise Exception("Invalid Comparision")
        if self.last + "," + self.first < \
                other.last + "," + other.first:
            return True
        return False


"""
    Read all address cards from addressbook.txt 
    and fill addresscards list
"""


def readaddressbook(addresscards=addresscards):
    global phonebook
    if phonebook is None or phonebook.closed:
        phonebook = open(phonebookname, 'r')

    """ We assume records are correctly stored in addressbook.txt file """
    firstandlastNameFromFile = phonebook.readline().rstrip()
    while firstandlastNameFromFile != "":
        first = firstandlastNameFromFile.split(" ")[0].strip()
        last = firstandlastNameFromFile.split(" ")[1].strip()
        street = phonebook.readline().rstrip()
        citycountryzip = phonebook.readline().rstrip()
        city = citycountryzip.split(',')[0]
        countryzip = citycountryzip.split(',')[1]
        country = countryzip.split(' ')[0]
        zip = countryzip.split(' ')[1]
        phone = phonebook.readline().rstrip()
        mobile = phonebook.readline().rstrip()
        firstandlastNameFromFile = phonebook.readline().rstrip()

        # (self,last,first,street,city,country,zip,phone,mobile)
        addresscard = AddressCard(last, first, street, city, country, zip, phone, mobile)

        addresscards.append(addresscard)
        addresscards.sort(key=lambda x: x.last + "," + x.first)
    phonebook.close()


def findAddress(lastname, firstname, addresscards):

    card = AddressCard(lastname, firstname,"","","","","","")

    try:
        j = addresscards.index(card)
        card = addresscards[j]

        print("AddressCard for %s %s found. Details below." % (lastname, firstname))
        print(str(card))
        return

    except Exception as e:
        True

    print("AddressCard for %s %s not found." % (lastname, firstname))

def main():
    readaddressbook(addresscards=addresscards)
    print("%d adress cards has been read" % len(addresscards))
    choice = 1
    while choice != 3:
        print("1) Look up a person by last name")
        print("2) Add a person to the address book.")
        print("3) Quit")
        choice = int(input("Enter your choice:"))

        if choice == 2:
            phonebook = open(phonebookname, 'a')
            lastName = str(input("LastName: "))
            firstName = str(input("FirstName: "))
            street = str(input("Street:"))
            citycountryzip = str(input("City,Country Zip:"))
            city = citycountryzip.split(',')[0]
            countryzip = citycountryzip.split(',')[1]
            country = countryzip.split(' ')[0]
            zip = countryzip.split(' ')[1]

            phone = str(input("Homephone:"))
            mobile = str(input("MobilePhone: "))

            addresscard = AddressCard(lastName, firstName, street, city, country, zip, phone, mobile)

            phonebook.write(str(addresscard))
            phonebook.close()

            addresscards.append(addresscard)
            addresscards.sort(key=lambda x: x.last + "," + x.first)

        if choice == 1:
            firstname = str(input("Please enter the first name "))
            lastname = str(input("Please enter the last name "))
            findAddress(lastname, firstname, addresscards)


if __name__ == "__main__":
    main()
