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
    
    

def customSortKey(country):
    return country[3]    
    
    
  
i = 0
countries = []
while i<len(populationList):
    countries.append((populationList[i][0], populationList[i][1], areaList[i][1], populationList[i][1]/areaList[i][1]))
    i += 1
    
countries.sort(key=customSortKey)
for country in countries:
    if country[0] == "Vatican City":
        precision = 2
    else:
        precision = 1
    print("{}\t{}\t{:.{}f}\t{}".format(country[0], int(country[1]), country[2], precision, country[3]))