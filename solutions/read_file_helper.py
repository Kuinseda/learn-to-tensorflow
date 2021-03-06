import numpy as np

fileText = "Fuzzy Wuzzy was a bear.  Fuzzy Wuzzy had no hair.  Fuzzy Wuzzy wasn't fuzzy, was he."
fileTextLength = len(fileText)
textLength = 5
iterations = int(fileTextLength / textLength)


def set(fileName, length):
    global fileText
    global textLength
    global iterations
    global fileTextLength

    with open(fileName, "r") as fileHandle:
        fileText = fileHandle.read()
        fileTextLength = len(fileText)

    textLength = length
    iterations = int(fileTextLength / textLength)


def getXY(fullindex):
    global fileText
    global textLength
    global iterations
    global fileTextLength
    index = (fullindex % iterations) * textLength
    x = fileText[index:index + textLength]
    y = fileText[index + 1:index + textLength + 1]
    x = [ord(c) for c in x]
    y = [ord(c) for c in y]
    return x, y, 1.0 * fullindex / iterations
