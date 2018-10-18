import sys

def prntShLine():
    print("#####################################")
 
    
def prntNumsLine(numbers):
    i = 0
    print("#", end="")
    while i<9:
        print(" " + numbers[i] + " ", end="")
        i += 1
        if (i%3==0):
            print("#", end="")
        else:
            print("|", end="")
    print()
            
            
def prntBorderLine():
    print("#---+---+---#---+---+---#---+---+---#")
         
         
         
def checkForExceptions(sudoku):
    if type(sudoku) != str:
        raise TypeError("TypeError: Illegal Sudoku type " + str(type(sudoku)))
    else:
        if len(sudoku) != 81:
            raise ValueError("ValueError: Illegal Sudoku length {} != 81".format(len(sudoku)))
        else:
            illegalChars = []
            for c in sudoku:
                if not("1" <= c <= "9"):
                    illegalChars.append(c)
            if len(illegalChars) == 0:
                return
            else:
                raise ValueError("ValueError: Illegal value(s) " + ', '.join(map(str, illegalChars)) + " for a Sudoku digit")

def printSudoku(sudoku):
    try:
        checkForExceptions(sudoku)
        prntShLine()
        i = 0
        linesPrinted = 0
        while i < 81:
            prntNumsLine(sudoku[i:i+9])
            i += 9
            linesPrinted += 1
            if (linesPrinted%3==0):
                prntShLine()
            else:
                prntBorderLine()
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    