
def allEvens(lst):
    n = []
    for i in lst:
        if i % 2 == 0:
            n.append(i)
    return n


def main():
    l = [1, 2, 3, 4, 32, 23, 23, 43]
    print(l)
    print(allEvens(l))
    l = []
    print(l)
    print(allEvens(l))
    l = [934,23, 34 ,23 ,33,44,99,101, 204, 2034]
    print(l)
    print(allEvens(l))


if __name__ == "__main__":
    main()