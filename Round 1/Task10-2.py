def list_bins(listItems, capacity):
    i = 0
    finalOutput = []
    while i < len(listItems):
        current = 0
        output = []
        while i < len(listItems):
            if listItems[i] + current > capacity:
                break
            output.append(listItems[i])
            current = listItems[i] + current
            i += 1
        finalOutput.append((output, current))
    return finalOutput