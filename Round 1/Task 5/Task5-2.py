def print_list(vals, n = None, k = 1):
    if n == None:
        n = len(vals) - 1
    if (k <= 0 or n <0):
        print("Illegal parameter n = {} or k = {}!".format(n, k))
        return
    i = 0
    while(i<=n) and (i<len(vals)):
        print("{}: {}".format(i, vals[i]))
        i += k