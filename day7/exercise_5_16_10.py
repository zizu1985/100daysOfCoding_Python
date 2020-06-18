import sympy


def sumIt(lst):
    s=0
    for l in lst:
        s = s + int(l)
    return s


def main():
    lst = [1, 2, 3, 4, 6]
    print("Sum of list %s is %d" % (lst,sumIt(lst)))
    primes = sympy.primerange(0,1000)
    lst = list(primes)
    print("Sum of list %s is %d" % (lst,sumIt(lst)))


if __name__ == "__main__":
    main()