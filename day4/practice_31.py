s = str(input("Enter sequence : "))
# elif in list comphrension
t = ''.join([i.lower() if i.isupper() else i.upper() if i.islower() else i for i in s])
print(t)