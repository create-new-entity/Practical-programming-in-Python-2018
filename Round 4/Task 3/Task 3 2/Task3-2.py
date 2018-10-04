from sys import argv


class Currencies:
    __slots__ = ("__currencyDic")
    
    def __init__(self, fileName):
        self.__currencyDic = {}
        with open(fileName) as inFile:
            for line in inFile:
                line = line.strip("\n")
                #print("Line: ", line)
                line = line.split("\t")
                self.__currencyDic[line[0]] = (line[0], line[1], float(line[2]), float(line[3]))
        
        
    @property
    def currencyDic(self):
        return self.__currencyDic
    @currencyDic.setter
    def name(self, currencyDic):
        self.__currencyDic = currencyDic
        
    def sortByName(self):
        return sorted(self.__currencyDic.keys())
        
    def sortByRate(self, currency):
        return currency[3]
        
        
    def listByName(self):
        sortedNames = self.sortByName()
        for key in sortedNames:
            print("{} {}".format(self.__currencyDic[key][0], self.__currencyDic[key][3]))
            
    def listByRate(self):
        sortedNames = self.sortByName()
        ratesByNames = []
        for key in sortedNames:
            ratesByNames.append(self.__currencyDic[key])
        for currency in sorted(ratesByNames, key = self.sortByRate):
            print("{} {}".format(currency[0], currency[3]))
            
    def convert(self, currA, x, currB):
        return self.__currencyDic[currB][2] * (self.__currencyDic[currA][3] * float(x))
            
        