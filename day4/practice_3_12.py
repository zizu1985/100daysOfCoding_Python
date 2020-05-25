s = input("Please enter a list of integers:")
lst = s.split()
count = 0
for e in lst:
    e_int = int(e)
    if (e_int % 2) == 0:
        count = count + 1
print("There were", count, " even integers in the list.")