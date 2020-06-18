

def ispalindrome(s):
    if len(s) in [0, 1]:
        return True
    niter = len(s) // 2
    for i in range(niter):
        a = s[i]
        b = s[len(s) - 1 - i]
        if a != b:
            return False
    return True


def main():
    print("%s is palindrom ? %r " % ("hello", ispalindrome("hello")))
    print("%s is palindrom ? %r" % ("radar", ispalindrome("radar")))
    print("%s is palindrom ? %r " % ("oko", ispalindrome("oko")))
    print("%s is palindrom ? %r " % ("dzwiek", ispalindrome("dzwiek")))
    print("%s is palindrom ? %r" % ("saippuakivikauppias", ispalindrome("saippuakivikauppias")))


if __name__ == "__main__":
    main()

