import sys

def print_list():
    i = 1
    while i<len(sys.argv):
        print(sys.argv[i])
        i += 1

        
sys.argv[1:] = sorted(sys.argv[1:])
print_list()
print()
sys.argv[1:] = sorted(sys.argv[1:], reverse = True)
print_list()