def wordLenFilter(fileName, wordLength):
  with open(fileName) as inFile:
    for line in inFile:
      for word in line.strip("\n").split():
        if len(word) == wordLength:
          yield word