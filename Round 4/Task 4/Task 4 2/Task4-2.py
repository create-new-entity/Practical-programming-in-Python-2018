from sys import argv


class Country:
    __slots__ = ("__name", "__population", "__area")

    def __init__(self, name, population, area):
        self.__name = name
        self.__population = population
        self.__area = area
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def population(self):
        return self.__population
    @population.setter
    def population(self, population):
        self.__population = population
        
    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self, area):
        self.__area = area
        
    def __gt__(self, other):
        return self.__area > other.area
        
    def __lt__(self, other):
        return self.__area < other.area
        
    def __str__(self):
        return "{} (pop.: {}, area: {})".format(self.name, self.population, self.area)
        
        
        
class Countries:
    __slots__ = ("__countriesList")
    
    
    def __init__(self, countriesFileName):
        self.__countriesList = []
        with open(countriesFileName) as inFile:
            for line in inFile:
                line = line.rstrip("\n")
                line = line.split("\t")
                self.__countriesList.append(Country(line[0], int(line[1]), float(line[2])))
                
    def sortByCountryName(self, countryObject):
        return countryObject.name
        
    def size(self):
        return len(self.__countriesList)
        
    def list(self):
        return sorted(self.__countriesList, key = self.sortByCountryName)

        
