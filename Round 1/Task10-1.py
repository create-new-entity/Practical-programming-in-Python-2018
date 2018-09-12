def print_bins(listItems, capacity):
    i = 0
    nthContainer = 0
    while i < len(listItems):
        current = 0
        output = ""
        firstItem = True
        while i < len(listItems):
            if listItems[i] + current > capacity:
                break
            if firstItem:
                firstItem = False
            else:
                output += " "
            output += str(listItems[i])
            current = listItems[i] + current
            i += 1
        nthContainer += 1
        output = "Container {}: " + output + " (total: {})"
        print(output.format(nthContainer, current))
