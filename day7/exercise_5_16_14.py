def factors(n):
    lfactors = []
    for i in range(1, n+1):
        if n % i == 0:
            lfactors.append(i)
    return lfactors


def main():
    print("Factors for %s is %s " % (26,factors(26)))


if __name__ == "__main__":
    main()