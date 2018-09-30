from sys import argv


def customSortKey(subString):
    return (len(subString), subString)


inputString = argv[1]
nStringsPerLine = int(argv[2])


subStrLength = 1
subStrings = []

while subStrLength <= len(inputString):
    startPosition = 0
    while startPosition < len(inputString) and subStrLength <= len(inputString[startPosition:startPosition+subStrLength]):
        subStr = inputString[startPosition:startPosition+subStrLength]
        subStrings.append(subStr)
        startPosition += 1
    subStrLength += 1

subStrings.sort(key = customSortKey)


i = 0
while i < len(subStrings):
    print(" ".join(map(lambda x: str(x), subStrings[i:i+nStringsPerLine])))
    i += nStringsPerLine

