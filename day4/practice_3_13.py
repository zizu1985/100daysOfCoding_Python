s = int(input("Enter integer"))
ret = 1
for i in range(1,s+1):
    ret = ret * i
print("%d ! = %d" % (s, ret))