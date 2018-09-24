
def indexDict(vals):
    output = {}
    
    for i, v in enumerate(vals):
        try:
            output[v].append(i)
        except KeyError:
            output[v] = [i]
    return output
    