class Rational:

    def __init__(self,numerator=1,denonimator=1):
        self.numerator = numerator
        self.denonimator = denonimator


    def getNumerator(self):
        return self.numerator


if __name__ == "__main__":
    rat = Rational(1, 4)
    print("Numerator is %d" % rat.getNumerator())
