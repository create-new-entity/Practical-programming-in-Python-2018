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


n = int(input("Enter the number of values: "))
if n <= 0:
    print()
    print("You gave zero numbers.")
else:
    fNumbers = []
    i = 0
    while i < n:
        fNumber = float(input("Enter the " + getOrdinal(i+1) + " value: "))
        fNumbers.append(fNumber)
        i += 1
    print()
    print("Minimum {}, maximum {}, sum {} and mean {}".format(min(fNumbers), max(fNumbers), sum(fNumbers), statistics.mean(fNumbers)))
 