import json
from sys import argv


def sortKey(elem):
    return elem["country"]
    
    
def insertGDP(gdpData):
    for countryData in data:
        if countryData["country"].strip() == gdpData[1].strip():
            countryData["gdp_per_capita"] = int(gdpData[2])
            return  



with open(argv[1]) as inFile:
    data = json.load(inFile)
    

with open(argv[2]) as inFile:
    for countryData in data:
      countryData["gdp_per_capita"] = "N/A"
      
    for line in inFile:
        line = line.strip()
        line = line.split("\t")
        line[2] = line[2].replace(",", "")
        insertGDP(line)
        
data.sort(key=sortKey)


with open(argv[3], "w") as outFile:
    json.dump(data, outFile, indent = 3, sort_keys = True)
        