def factors(n):
    lfactors = []
    for i in range(1, n+1):
        if n % i == 0:
            lfactors.append(i)
    return lfactors


def sumFactors(n):
    lfactors = factors(n)
    s = 0
    for l in lfactors:
        s = s + int(l)
    return s


def main():
    print("Sum Factors for %s , % s is %s " % (26,factors(26),sumFactors(26)))


if __name__ == "__main__":
    main()