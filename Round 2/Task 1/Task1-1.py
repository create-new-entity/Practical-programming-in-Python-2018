import sys

i = 1
while i<len(sys.argv):
    print(("{}: ".format(i)) + sys.argv[i] + " (length: " + str(len(sys.argv[i])) + ")")
    i += 1    