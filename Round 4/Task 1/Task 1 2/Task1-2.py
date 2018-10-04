from sys import argv


inputEncoding = argv[1]
outputEncoding = argv[2]
inputFileName = argv[3]


try:
    with open(inputFileName, encoding = inputEncoding) as inputFile:
        lines = inputFile.readlines()
    
    with open(inputFileName, "w", encoding = outputEncoding) as outputFile:
        for line in lines:
            print(line, file = outputFile, end="")


except OSError:
    print("Error opening", inputFileName)

except UnicodeDecodeError:
    print("Error reading", inputFileName,"with", inputEncoding)

except UnicodeEncodeError:
    print("Error writing", inputFileName, "with", outputEncoding)
    with open(inputFileName, "w", encoding = inputEncoding) as outputFile:
        for line in lines:
            print(line, file = outputFile, end="")
