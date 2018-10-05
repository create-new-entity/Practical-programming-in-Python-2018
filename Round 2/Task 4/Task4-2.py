



def multiplicationTable(a, b, c, d):
    data = list(range(a,b+1))
    dataWidths = []
    maxWidths = []
    tableWidth = b - a + 1
    tableHeight = d - c + 1
    
    firstColumnMaxWidth = -1
    for val in range(c, d+1):
        if firstColumnMaxWidth < len(str(val)):
            firstColumnMaxWidth = len(str(val))
        for firstRowItem in range(a, b+1):
            data.append(val*firstRowItem)
            dataWidths.append(len(str(val*firstRowItem)))
            
    
    for nthColumn in range(0, tableWidth):
        max = -1
        for nthRow in range(0, tableHeight):
            if max < dataWidths[nthRow*tableWidth+nthColumn]:
                max = dataWidths[nthRow*tableWidth+nthColumn]
        maxWidths.append(max)
                                                                                #
    emptyCell = "".join([" "] * firstColumnMaxWidth)                            #
    print(emptyCell, end="")                                                    #   
    for nthColumn in range(0, tableWidth):                                      #   Print the first row  
        print(" ", end="")                                                      #
        print("{:{}d}".format(data[nthColumn], maxWidths[nthColumn]), end="")   #        
    print()                                                                     #
    
    
    nthRow = 1                                                                                          #
    for val in range(c,d+1):                                                                            #
        print("{:{}d}".format(val, firstColumnMaxWidth), end="")                                        #   
        for nthColumn in range(0, tableWidth):                                                          #   Print rest of the rows
            print(" ", end="")                                                                          #
            print("{:{}}".format(data[nthRow*tableWidth+nthColumn], maxWidths[nthColumn]), end="")      #
        print()                                                                                         #
        nthRow += 1
 
    