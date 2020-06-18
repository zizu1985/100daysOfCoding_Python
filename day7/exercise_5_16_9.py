

def unzip(sList):
    firstList = []
    secList = []
    for i in range(len(sList)):
        t = sList[i]
        firstList.append(t[0])
        secList.append(t[1])
    return (firstList, secList)


def main():
    rList = [(1,2), (2,3), (3,1)]
    (firstList, secList) = unzip(rList)
    print("First list " + str(firstList))
    print("Second list " + str(secList))
    print("Source list " + str(rList))

    rList = [(1, 1), (2, 2), (3, 3), (4, 4)]
    (firstList, secList) = unzip(rList)
    print("First list " + str(firstList))
    print("Second list " + str(secList))
    print("Source list " + str(rList))


if __name__ == '__main__':
    main()