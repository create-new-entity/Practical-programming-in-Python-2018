import sys

inputs = sys.argv[1:]
i = 0
for val in inputs:
    print(("{:{}d}: ".format(i+1, len((str(len(inputs))))) + val + " (count: " + str(inputs.count(val)) + ")"))
    i += 1
