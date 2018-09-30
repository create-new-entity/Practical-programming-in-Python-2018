from sys import argv

rates = {}


def checkFloat(number):
    try:
        number = float(number)
        return True
    except:
        return False
       

def saveRate(command):
    fromCurrency = command[1].upper()
    toCurrency = command[3].upper()
    fromRate = float(command[0])
    toRate = float(command[2])
    rates[(fromCurrency, toCurrency)] = (fromRate, toRate)  

    
def getSortedRatesList():
    ratesList = list(rates.keys())
    ratesList.sort()
    return ratesList
    

def printRates():
    ratesList = getSortedRatesList()
    if len(ratesList) <= 0:
        print("No rates defined yet!")
        return
    
    for item in ratesList:
        print("{}\t{}\t{}\t{}".format(rates[item][0], item[0], rates[item][1], item[1]))
        
        
def printRatesInFile(outputFileName):
    ratesList = getSortedRatesList()
    with open(outputFileName, "w") as outputFile:
        if len(ratesList) <= 0:
            print("No rates defined yet!", file = outputFile)
            return
    
        for item in ratesList:
            print("{}\t{}\t{}\t{}".format(rates[item][0], item[0], rates[item][1], item[1]), file = outputFile)
            
        
def checkAvailability(fromCurrency, toCurrency):
    fromCurrency = fromCurrency.upper()
    toCurrency = toCurrency.upper()
    
    if(((fromCurrency, toCurrency) in rates) or (((fromCurrency, "EUR") in rates) and (("EUR", toCurrency) in rates))):
        return True
    return False
    
    
def convertCurrency(amount, fromCurrency, toCurrency):
    amount = float(amount)
    fromCurrency = fromCurrency.upper()
    toCurrency = toCurrency.upper()
    convertedAmount = amount
    
    if (fromCurrency, toCurrency) in rates:
        rate = rates[(fromCurrency, toCurrency)][1] / rates[(fromCurrency, toCurrency)][0]
    else:
        rate = rates[(fromCurrency, "EUR")][1] / rates[(fromCurrency, "EUR")][0]
        convertedAmount = amount * rate
        rate = rates[("EUR", toCurrency)][1] / rates[("EUR", toCurrency)][0]
    convertedAmount = rate * convertedAmount
    
    print("{} {} = {:.2f} {}".format(amount, fromCurrency, convertedAmount, toCurrency))


while True:
    command = input("Give a command: ")
    command = command.split()
    
    if len(command) == 4:
        if(checkFloat(command[0]) == False) or (checkFloat(command[2]) == False):
            print("Illegal command!")
        else:
            saveRate(command)
        
    elif len(command) == 2:
        if command[0] == "read":
            with open(command[1]) as inFile:
                for line in inFile.readlines():
                    saveRate(line.split())
        elif command[0] == "write":
            printRatesInFile(command[1])
            
    
    elif len(command) == 1:
        if command[0] == "rates":
            printRates()
        elif command[0] == "quit":
            break
        else:
            print("Illegal command!")
    elif len(command) == 3:
        if checkFloat(command[0]):
            if checkAvailability(command[1], command[2]):
                convertCurrency(command[0], command[1], command[2])
            else:
                print("No {}-{} rate available!".format((command[1]).upper(), (command[2]).upper()))
        else:
            print("Illegal command!")
    else:
        print("Illegal command!")
                
        
        