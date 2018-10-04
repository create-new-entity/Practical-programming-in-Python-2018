from sys import argv


inputFileName = argv[1]
outputFileName = argv[2]

uniqueNonWhiteSpaceCharacters = []

with open(inputFileName) as inputFile:
    for line in inputFile.readlines():
        line = line.strip()
        for word in line:
            word = word.strip()
            for letter in word:
                letter = letter.strip()
                if letter not in uniqueNonWhiteSpaceCharacters:
                    uniqueNonWhiteSpaceCharacters.append(letter)
                    
uniqueNonWhiteSpaceCharacters = " ".join(uniqueNonWhiteSpaceCharacters)
uniqueNonWhiteSpaceCharacters = uniqueNonWhiteSpaceCharacters.strip()

with open(outputFileName, "w") as outputFile:
    print(uniqueNonWhiteSpaceCharacters, file = outputFile)
    