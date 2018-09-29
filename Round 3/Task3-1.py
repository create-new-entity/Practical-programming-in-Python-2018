from sys import argv


def inputToTupleList(inputFile):
    list = []
    for line in inputFile:
        splittedList = line.strip("\n").split("\t")
        list.append((splittedList[0], float(splittedList[1].replace(",",""))))
        list.sort()
    return list
    

with open(argv[1]) as populationFile:
    populationList = inputToTupleList(populationFile)
    
    
with open(argv[2]) as areaFile:
    areaList = inputToTupleList(areaFile)
    
    
i = 0
while i<len(populationList):
    if populationList[i][0] == "Vatican City":
        precision = 2
    else:
        precision = 1
    print("{}\t{}\t{:.{}f}".format(populationList[i][0], int(populationList[i][1]), areaList[i][1], precision))
    i += 1