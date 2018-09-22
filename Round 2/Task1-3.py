import sys

def createList():
    i = 1
    inputs = []
    while i<len(sys.argv):
        inputs.append((sys.argv[i],i));
        i += 1
    return inputs

        
inputs = createList()
inputs.sort()

for x in inputs:
    print(x[0] + " (index: " + str(x[1]) + ")")
