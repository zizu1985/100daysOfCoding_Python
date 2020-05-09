'''

How much did the item cost : 65.64
How much did the person give you: 100.00
The person ’s change is $34 .36
The bills or the change should be:
1 twenties
1 tens
0 fives
4 ones
1 quarters1 dimes
0 nickels
1 pennies

2020.05.08 tziss85@gmail.com
    Printed only non zero bills & coins


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
    if twenties > 0:
        msg = "%d twenties"
        if twenties == 1:
            msg = "%d twenty"
        print(msg % twenties)
    if tens > 0:
        msg = "%d tens"
        if tens == 1:
            msg = "%d ten"
        print(msg % tens)
    if fives > 0:
        msg = "%d fives"
        if fives == 1:
            msg = "%d five"
        print(msg % fives)
    if ones > 0:
        msg = "%d ones"
        if ones == 1:
            msg = "%d one"
        print(msg % ones)
    if quarters > 0:
        msg = "%d quarters"
        if quarters == 1:
            msg = "%d quarter"
        print(msg % quarters)


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
    quarters = (int)(remain / 0.2)
else:
    quarters = 0

remain = remain - quarters * 0.25

print_change_bills()

if remain > 0.00:
    print("Bill is %1.2f" % remain)

