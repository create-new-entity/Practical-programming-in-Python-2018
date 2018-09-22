import sys

inputs = sys.argv[1:]
inputsSet = set(inputs)
tuples = []


def comp(v):
    return v[1]


for val in inputsSet:
    tuples.append((val, inputs.index(val)+1))
    
tuples.sort()
tuples2 = sorted(tuples, key=comp)

for val in tuples:
    print(("{:{}}: ".format(val[1], len(str(tuples2[len(tuples2)-1][1])))) + val[0] + " (count: " + str(inputs.count(val[0])) + ")")

