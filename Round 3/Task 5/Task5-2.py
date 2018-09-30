from sys import argv


def sortLength(subString):
    return len(subString)
    
def sortAlphabetically(subString):
    return subString


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

subStrings.sort(key = sortAlphabetically)           #Do the secondary first
subStrings.sort(key = sortLength, reverse = True)


i = 0
while i < len(subStrings):
    print(" ".join(map(lambda x: str(x), subStrings[i:i+nStringsPerLine])))
    i += nStringsPerLine

