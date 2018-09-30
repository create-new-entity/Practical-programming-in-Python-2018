from sys import argv

lenOfLongestTeamName = 0
matchesInfo = []


def countryNameSort(item):
    return item[0]
    
def scoredSort(item):
    return item[8]
    
def goalDifferenceSort(item):
    return item[7]
    
def pointsSort(item):
    return item[6]


def calculatePoint(nWins, nTies):
    return 3 * nWins + nTies
    
def calculateGoalRules(scoredAndConsumed):
    scoredAndConsumed = scoredAndConsumed.split("-")
    scored = int(scoredAndConsumed[0])
    consumed = int(scoredAndConsumed[1])
    return (scored-consumed, scored)


with open(argv[1]) as inputFile:
    for line in inputFile.readlines():
        line = line.strip("\n")
        line = line.split("\t")
        if(len(line[0]) > lenOfLongestTeamName):
            lenOfLongestTeamName = len(line[0])
        matchesInfo.append((line[0], (int(line[1]) + int(line[2]) + int(line[3])), int(line[1]), int(line[2]), int(line[3]), line[4], calculatePoint(int(line[1]), int(line[2])), calculateGoalRules(line[4])[0], calculateGoalRules(line[4])[1]))

        
matchesInfo.sort(key = countryNameSort)
matchesInfo.sort(key = scoredSort, reverse = True)
matchesInfo.sort(key = goalDifferenceSort, reverse = True)
matchesInfo.sort(key = pointsSort, reverse = True)


for item in matchesInfo:
    print("{:{}}{:3}{:3}{:3}{:3}{:>6}{:3}".format(item[0], lenOfLongestTeamName, item[1], item[2], item[3], item[4], item[5], item[6]))

