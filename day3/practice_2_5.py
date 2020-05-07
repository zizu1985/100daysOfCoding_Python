citizen=input("Are you citized on United States?")
age=input("Have you 35 years or more?")
residence=input("Have you 14 or more years of residency in USA?")

youcanrun=True
if citizen == 'No':
    youcanrun = False
if age == 'No':
    youcanrun = False
if residence == 'No':
    youcanrun = False

if youcanrun:
    print('You could run for president.')
else:
    print("You could not run for president.")