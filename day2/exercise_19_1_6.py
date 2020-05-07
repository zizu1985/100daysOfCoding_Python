'''

How much did the item cost : 65.64
How much did the person give you: 100.00
The person ’s change is $34 .36
The bills or the change should be:
1 twenties
1 tens
0 fives
4 ones
1 quarters
1 dimes
0 nickels
1 pennies

'''
cost=float(input("How much did the item cost : "))
money=float(input("How much did the person give you :"))
change = money - cost
print("The persons' change is %1.2f" % change)

remain = change
twenties = 0
tens = 0
fives = 0
ones = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

def print_change_bills():
    print("%d twenties" % twenties)
    print("%d tens" % tens)
    print("%d fives" % fives)
    print("%d ones" % ones)
    print("%d quarters" % quarters)

if remain >= 20 :
    twenties = int(remain) // 20
else:
    twenties = 0

remain = remain - 20 * twenties
if remain == 0:
    print_change_bills()
    exit(0)

if remain >= 10:
    tens = int(remain) // 10
else:
    tens = 0

remain = remain - 10 * tens
if remain == 0:
    print_change_bills()
    exit(0)

if remain >= 5:
    fives = int(remain) // 5
else:
    fives = 0

remain = remain - 5 * fives
if remain == 0:
    print_change_bills()
    exit(0)

if remain >= 1:
    ones = int(remain)
else:
    ones = 0

remain = (float)(remain - ones)
if remain == 0:
    print_change_bills()
    exit(0)

if remain >= 0.25:
    quarters = (int)(remain / 0.25)
else:
    quarters = 0

remain = remain - quarters * 0.25

print_change_bills()

if remain > 0.00:
    print("Bill is %1.2f" % remain)

