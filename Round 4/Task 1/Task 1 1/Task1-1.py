from sys import argv


populationFile = argv[1]
areaFile = argv[2]
outputFile = argv[3]


def readFileInfo(fileName):
    fileInfo = {}
    with open(fileName) as inFile:
        for line in inFile:
            line = line.split("\t")
            line[1] = line[1].strip("\n")
            line[1] = line[1].replace(",", "")
            fileInfo[line[0]] = line[1]
    
    return fileInfo
    
def writePopulationAndArea(populationDic, areaDic, outputFileName):
    with open(outputFileName, "w") as outputFile:
        for item in populationDic.items():
            print("{}\t{}\t{}".format(item[0], item[1], float(areaDic[item[0]])), file = outputFile)
     
            
                       
populationDic = readFileInfo(populationFile)
areaDic = readFileInfo(areaFile)
writePopulationAndArea(populationDic, areaDic, outputFile)
