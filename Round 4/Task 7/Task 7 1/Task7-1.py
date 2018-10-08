from sys import argv


def pickNumbers(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            for word in line.strip().split():
                try:
                    yield float(word)
                except:
                    continue
                 
                    