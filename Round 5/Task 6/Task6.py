from sys import argv

class SudokuException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    
    def __str__(self):
        return "[SudokuException] " + Exception.__str__(self)
        

class SudokuTypeError(SudokuException):
    def __init__(self, message):
        super().__init__(message)
      
    def __str__(self):
        return "[SudokuTypeError] " + Exception.__str__(self)
      
        
class SudokuValueError(SudokuException):
    def __init__(self, char):
        if char == "0":
            super().__init__("The number {} is not legal in Sudoku".format(char))
        else:
            super().__init__("The character {} does not represent a digit".format(char))
            
    def __str__(self):
        return "[SudokuValueError] " + Exception.__str__(self)

         
         
def checkForExceptions(sudoku):
    if type(sudoku) != str:
        raise SudokuTypeError("Illegal type " + str(type(sudoku)))
    else:
        if len(sudoku) != 81:
            raise SudokuTypeError("Illegal length {} != 81".format(len(sudoku)))
        else:
            for c in sudoku:
                if not("1" <= c <= "9"):
                    raise SudokuValueError(c)

def printSudoku(sudoku):
    checkForExceptions(sudoku)
    