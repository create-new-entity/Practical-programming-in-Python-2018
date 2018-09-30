

from sys import argv


def getRowsFromInput(fileName):
    rows = []
    with open(fileName) as inFile:
        for line in inFile.readlines():
            if not((line == "#####################################") or (line =="#---+---+---#---+---+---#---+---+---#")):
                i = 0
                row = []
                for c in line:
                    if "1" <= c <= "9":
                        row.append(c)
                if len(row) > 0:
                    rows.append(row)
    return rows


    
def checkRows(rows):
    illegalRows = []
    for row in rows:
        for item in row:
            if row.count(item) > 1:
                illegalRows.append(rows.index(row)+1)
                break
                
    return illegalRows
    
    
def checkColumns(rows):
    illegalColumns = []
    i = 0
    while i < 9:
        column = []
        for row in rows:
            column.append(row[i])
            if column.count(row[i]) > 1:
                illegalColumns.append(i+1)
                break
        i += 1
        
    return illegalColumns
    
    
    
def checkSubGrid(subGridItems):
    for item in subGridItems:
        if subGridItems.count(item) > 1:
            return False
    return True
    
    
def checkGrid(rows):
    illegalSubGrids = []
    subGridRow = 0
    subGridStartRow = 0
    
    while subGridRow < 3:
        subGridColumn = 0
        subGridNthRowColumnStart = 0
        while subGridColumn < 3:
            rowAfterCurrentSubGridLastrow = subGridStartRow + 3
            i = subGridStartRow
            subGridItems = []
            while i < rowAfterCurrentSubGridLastrow:
                subGridItems += rows[i][subGridNthRowColumnStart:subGridNthRowColumnStart+3]
                i += 1
            subGridNthRowColumnStart += 3
            if checkSubGrid(subGridItems) == False:
                illegalSubGrids.append([subGridRow + 1, subGridColumn + 1])
            subGridColumn += 1
        subGridStartRow += 3
        subGridRow += 1
    
    return illegalSubGrids
            
            
                
                
def printListItems(list):
    if len(list) == 0:
        return
    for item in list:
        print(" " + str(item), end = "")
    print()

                
                
def checkSudoku(fileName):
    
    rows = getRowsFromInput(fileName)
    illegalRows = checkRows(rows)
    illegalColumns = checkColumns(rows)
    illegalSubGrids = checkGrid(rows)
    
    if len(illegalColumns) == 0 and len(illegalRows) == 0 and len(illegalSubGrids) == 0:
        print("The sudoku solution is legal")
    else:
        print("Illegal rows:", end = "")
        printListItems(illegalRows)
        print("Illegal columns:", end = "")
        printListItems(illegalColumns)
        print("Illegal subgrids:", end = "")
        printListItems(illegalSubGrids)
    