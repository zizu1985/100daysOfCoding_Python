# 3. Split Sentence into words
def splitSentence(sentence):
    return sentence.split()


# 1. Make first letter in list of words uppercase
def capitalizeWord(words):
    outWords = []
    for word in words:
        outWords.append(word.title())
    return outWords


# 2. Build sentence from list of capitalized words
def buildcaptilizedSentence(words):
    return ' '.join(words)


def main():
    sentence=str(input("Please provide input sentence : "))
    words = splitSentence(sentence)
    lCapWords = capitalizeWord(words)
    outSentence = buildcaptilizedSentence(lCapWords)
    print("Output sentence is : %s " % outSentence)


if __name__ == "__main__":
    main()