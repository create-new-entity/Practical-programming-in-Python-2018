import sys


inputs = list(sys.argv[1])


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
         
         
prntShLine()
i = 0
linesPrinted = 0
while i < 81:
    prntNumsLine(inputs[i:i+9])
    i += 9
    linesPrinted += 1
    if (linesPrinted%3==0):
        prntShLine()
    else:
        prntBorderLine()   