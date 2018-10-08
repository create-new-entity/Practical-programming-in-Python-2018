from sys import argv

def readTextFiles(fileName):
    fileWords = []
    with open(fileName) as inFile:
        for line in inFile:
            for word in line.rstrip("\n").split():
                fileWords.append(word)
    return fileWords
    
    
def makeSet(fileWords):
    wordsList = []
    i = 0
    while i+k <= len(fileWords):
        wordsList.append(tuple(fileWords[i:i+k]))
        i += 1
    return set(wordsList)
    
    
k = int(argv[1])
inputFile1 = argv[2]
inputFile2 = argv[3]

file1Words = readTextFiles(inputFile1)
file2Words = readTextFiles(inputFile2)

setA = makeSet(file1Words)
setB = makeSet(file2Words)

print("JAC({}): {}".format(k, round(len(setA & setB) / len(setA | setB), 4)))

