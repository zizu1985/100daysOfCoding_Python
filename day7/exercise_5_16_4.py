
def isEven(n=0):
    return int(n) % 2

def main():
    for i in [0,2,3,4,45,23,5434.3453,23] :
        if isEven(i):
            print("isEven(%s) is True" % i)
        else:
            print("isEven(%s) is False" % i)

if __name__ == "__main__":
    main()