import sys

inputs = sys.argv[1:]
inputsSet = set(inputs)
tuples = []

for val in inputsSet:
    tuples.append((inputs.index(val)+1, val))
    
tuples.sort()
for val in tuples:
    print(("{:{}}: ".format(val[0], len(str(tuples[len(tuples)-1][0])))) + val[1] + " (count: " + str(inputs.count(val[1])) + ")")

