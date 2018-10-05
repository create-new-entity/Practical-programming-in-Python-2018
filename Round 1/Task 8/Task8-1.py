import statistics


n = int(input("Enter the number of values: "))
if n <= 0:
    print()
    print("You gave zero numbers.")
else:
    fNumbers = []
    i = 0
    while i < n:
        fNumber = float(input("Enter a value: "))
        fNumbers.append(fNumber)
        i += 1
    print()
    print("Minimum {}, maximum {}, sum {} and mean {}".format(min(fNumbers), max(fNumbers), sum(fNumbers), statistics.mean(fNumbers)))
 