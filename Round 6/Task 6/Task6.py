import re
from sys import argv

def listSeqs(typeStr, filename):
    mRNAPattern = '(mRNA\s*(complement\()?(join\()?)((((\d{6})\.\.(\d{6}))[,\s\t\n]*)+)'
    genePattern = '(gene\s*(complement\()?(join\()?)((((\d{6})\.\.(\d{6}))[,\s\t\n]*)+)'
    cdsPattern = '(CDS\s*(complement\()?(join\()?)((((\d{6})\.\.(\d{6}))[,\s\t\n]*)+)'
    rangePattern = '(\d{6}\.\.\d{6})'

    pattern = ''

    if(typeStr == "mRNA"):
        pattern = mRNAPattern
    elif(typeStr == "gene"):
        pattern = genePattern
    else:
        pattern = cdsPattern

    with open(filename) as inFile:
        contents = inFile.read()
    matches = re.findall(pattern, contents)

    for match in matches:
        if (match[1] != ""):
            print(typeStr + " complemented interval(s):")
        else:
            print(typeStr + " interval(s):")
        ranges = re.findall(rangePattern, match[3])
        for range in ranges:
            range = range.replace("..", " --> ")
            print("  " + range)
        print()
