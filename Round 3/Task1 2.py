


def indexDict(vals):
    output = {}
    valSet = set(vals)
    
    for val in valSet:
        for i, v in enumerate(vals):
            if v == val:
                output[val] = i
                break
    
    return output
    
  