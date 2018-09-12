def print_ints(n, k = 1, sep = " "):
    if k<=0:
        print("Illegal parameter k = {}!".format(k))
        return
    if n<0:
        k = -k
    first = 1
    current = 0
    currentStr = ""
    while (0 <= current <= n) or (n <= current <= 0):
        if first:
            first = 0
        else:
            currentStr += sep
        currentStr += str(current)
        current += k
    print(currentStr)