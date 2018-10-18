import json
from sys import argv

def sortKey(elem):
    return elem["country"]


with open(argv[1]) as inFile:
    data = []
    for line in inFile:
        dic = {}
        line.strip("\n")
        line = line.split("\t")
        dic["area"] = float(line[2])
        dic["country"] = line[0]
        dic["population"] = int(line[1])
        data.append(dic)
        
        
data.sort(key=sortKey)

with open(argv[2], "w") as outFile:
    json.dump(data, outFile, indent=3, sort_keys=True)
