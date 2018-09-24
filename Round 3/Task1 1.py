


def indexDict(vals):
    output = {}
    valSet = set(vals)
    
    for val in valSet:
        for i, v in enumerate(reversed(vals)):
            if v == val:
                lastIndex = len(vals) - 1 - i
                output[val] = lastIndex
                break
    
    return output
    
  