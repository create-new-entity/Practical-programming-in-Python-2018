from sys import argv


longestLineLength = 0
wordCount = 0
longestWordLength = 0
allCharCount = 0
nonWhiteSpaceCharCount = 0

with open(argv[1]) as inFile:
    lines = inFile.readlines()

for line in lines:
    allCharCount += len(line)
    if(len(line.rstrip("\n")) > longestLineLength):
        longestLineLength = len(line.rstrip("\n"))
    line = line.rstrip("\n").split(" ")
    if(len(line) == 1) and (line[0] == ''):
        continue
    for word in line:
        if(len(word) > longestWordLength):
            longestWordLength = len(word)
        nonWhiteSpaceCharCount += len(word)
    wordCount += len(line)
    
    
print("Lines:", len(lines))    
print("Max line length:", longestLineLength)
print("Words:", wordCount)
print("Max word length:", longestWordLength)
print("All characters:", allCharCount)
print("Non-whitespace:", nonWhiteSpaceCharCount)

