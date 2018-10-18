import json
from sys import argv

with open(argv[1]) as inFile:
    workersData = json.load(inFile)

workers = workersData["workers"]
checkOuts = workersData["checked out"]
checkIns = workersData["checked in"]



def extractData(workerId, checkInOrOutList):
    extractedData = []
    for item in checkInOrOutList:
        if item["worker id"] == workerId:
            extractedData.append(item["time"])
    return extractedData


def getHour(timeString):
    timeString = timeString.split("T")
    timeString = timeString[1].split(":")
    return float(timeString[0])


def calculateWage(worker, checkedInTimes, checkedOutTimes):
    i = 0
    totalHours = 0
    while (i<len(checkedInTimes)):
        checkInHour = getHour(checkedInTimes[i])
        checkOutHour = getHour(checkedOutTimes[i])
        if(checkOutHour - checkInHour < 0):
            hours = checkOutHour - checkInHour + 24
        else:
            hours = checkOutHour - checkInHour
        totalHours += hours
        i += 1
    wage = float(worker["hourly wage"])
    totalPay = wage * totalHours
    return (worker["name"], worker["id"], totalHours, worker["hourly wage"], totalPay)



outputData = []

for worker in workers:
    checkedInTimes = extractData(worker["id"], checkIns)
    checkedOutTimes = extractData(worker["id"], checkOuts)
    checkedInTimes.sort()
    checkedOutTimes.sort()
    outputData.append(calculateWage(worker, checkedInTimes, checkedOutTimes))

outputData.sort()
for output in outputData:
    print("{} {}: {:.1f} hours, hourly wage {:.1f}, total pay {:.1f}".format(output[1], output[0], output[2], output[3], output[4]))