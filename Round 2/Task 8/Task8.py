

def stringSearch(string, text, caseSensitive):
    lines = text.split("\n")
    nthLine = 0
    occurancePositions = []
    
    for line in lines:
        findFrom = 0
        if caseSensitive == False:
            line = line.lower()
            string = string.lower()
        while line.find(string, findFrom) != -1:
            foundAt = line.find(string, findFrom)
            occurancePositions.append((nthLine+1, foundAt+1))
            findFrom = foundAt+len(string)
        nthLine += 1
    return occurancePositions
    
            