from sys import argv


class Currency:
    __slots__ = ("__name", "__fullName", "__euroRate")
    
    def __init__(self, name, fullName, euroRate):
        self.__name = name
        self.__fullName = fullName
        self.__euroRate = float(euroRate)
        
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
        
    @property
    def fullName(self):
        return self.__fullName
    @fullName.setter
    def fullName(self, fullName):
        self.__fullName = fullName
        
    @property
    def euroRate(self):
        return self.__euroRate
    @euroRate.setter
    def euroRate(self, euroRate):
        self.__euroRate = euroRate
        

def loadCurrencies(fileName):
    currencyDic = {}
    with open(fileName) as inFile:
        for line in inFile:
            line = line.rstrip("\n")
            line = line.split("\t")
            currencyDic[line[0]] = Currency(line[0], line[1], line[3])
    
    return currencyDic
    
    
if __name__ == "__main__":
    with open(argv[1]) as inFile:
        fullNames = []
        for line in inFile:
            line = line.split("\t")
            fullNames.append(line[1])
        for fullName in sorted(fullNames):
            print(fullName)