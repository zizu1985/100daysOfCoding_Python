

def zip(fList, sList):
    rList = []
    if len(fList) != len(sList):
        return fList
    for i in range(len(fList)):
        t = (fList[i],sList[i])
        rList.append(t)
    return rList


def main():
    fList = [1, 2, 3]
    sList = [2, 3, 2]
    rList = zip(fList, sList)
    print("First list " + str(fList))
    print("Second list " + str(sList))
    print("Return list " + str(rList))

    fList = [1, 2, 3, 4]
    sList = [2, 3, 2]
    rList = zip(fList, sList)
    print("First list " + str(fList))
    print("Second list " + str(sList))
    print("Return list " + str(rList))


if __name__ == '__main__':
    main()