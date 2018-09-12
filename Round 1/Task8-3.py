import statistics

def getOrdinal(nthNumber):
    if 11 <= nthNumber <= 19:
        return str(nthNumber) + "th"
    else:
        if nthNumber % 10 == 1:
            return str(nthNumber) + "st"
        elif nthNumber % 10 == 2:
            return str(nthNumber) + "nd"
        elif nthNumber % 10 == 3:
            return str(nthNumber) + "rd"
        else:
            return str(nthNumber) + "th"

            
i = 0
inputNumbers = []
while True:
    nthNumber = input("Enter the " + getOrdinal(i+1) + " value (or give \"end\" to stop): ")
    if nthNumber == "end":
        break
    try:
        nthNumber = float(nthNumber)
        inputNumbers.append(nthNumber)
        i += 1
    except:
        print("Enter a float or \"end\"!")    

print()
if len(inputNumbers) > 0:
    print("Count {}, minimum {}, maximum {}, sum {} and mean {}".format(len(inputNumbers), min(inputNumbers), max(inputNumbers), sum(inputNumbers), statistics.mean(inputNumbers)))

else:
    print("You gave zero numbers.")
    
 