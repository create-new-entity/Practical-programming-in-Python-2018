def print_list(vals, a = 0, b = None, k = 1):
    if b == None:
        b = len(vals) - 1
    if (k <= 0 or b < 0 or not(0<=a<=b)):
        print("Illegal parameter a = {}, b = {} or k = {}!".format(a, b, k))
        return
    i = a
    while(i<=b) and (i<len(vals)):
        print("{}: {}".format(i, vals[i]))
        i += k