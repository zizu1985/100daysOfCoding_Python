import sympy.ntheory.primetest as primetest


def isPrime(n):
    return primetest.isprime(n)


def main():
    print("%s is Prime ? %r" % (1, isPrime(1)))
    print("%s is Prime ? %r" % (101, isPrime(101)))
    print("%s is Prime ? %r" % (46, isPrime(46)))


if __name__ == "__main__":
    main()

