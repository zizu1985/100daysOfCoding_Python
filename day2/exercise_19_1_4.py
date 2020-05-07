'''

Write a program that converts US Dollars to a Foreign Currency. You can do this
by finding the exchange rate on the internet and then prompting for the exchange
rate in your program. When you run the program it should look exactly like this:

What i s the amount of US Dollars you wish to convert ? 31.67
What i s the current exchange rate
(1 US Dollar equals what i n the Foreign Currency )? 0.9825
The amount i n the Foreign Currency i s $31 .12

'''

dollars=float(input("What os the amount of US Dollars you wish to convert ?"))
exrate=float(input("What is the current exchange rate (1 US Dollar equals what i n the Foreign Currency)?"))
print("The amount in the Foreign Currency is %1.2f" % (dollars * exrate))