import sympy


def recursiveSumIt(lst):
    if len(lst) == 1:
        return lst[0]
    return recursiveSumIt(lst[1:]) + lst[0]


def main():
    lst = [1, 2]
    print("Sum of list %s is %d" % (lst,recursiveSumIt(lst)))
    primes = sympy.primerange(0,1000)
    lst = list(primes)
    print("Sum of list %s is %d" % (lst,recursiveSumIt(lst)))


if __name__ == "__main__":
    main()