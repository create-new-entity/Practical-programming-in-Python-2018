
def multiplicationTable(a, b, c, d):
    maxDigitsLen = len(str(b*d))+1
    emptyCell = "".join([" "] * maxDigitsLen)
    
    print(emptyCell, end="")
    for val in range(a, b+1):
        print("{:{}d}".format(val, maxDigitsLen), end="")
    print()
    for val in range(c, d+1):
        print("{:{}d}".format(val, maxDigitsLen), end="")
        for firstRowItem in range(a, b+1):
            print("{:{}d}".format(val*firstRowItem, maxDigitsLen), end="")
        print()
    