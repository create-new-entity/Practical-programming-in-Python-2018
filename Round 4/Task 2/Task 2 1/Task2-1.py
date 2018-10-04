


class Car:
    __slots__ = ("__make", "__model", "__year", "__mileage")
    
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        
        
    @property
    def make(self):
        return self.__make
        
    @make.setter
    def make(self, make):
        self.__make = make
        
    
    @property
    def model(self):
        return self.__model
        
    @model.setter
    def model(self, model):
        self.__model = model
        
    
    @property
    def year(self):
        return self.__year
        
    @year.setter
    def year(self, year):
        self.__year = year
        
    
    @property
    def mileage(self):
        return self.__mileage
        
    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage
        
    
    def __str__(self):
        return "Make: {}\nModel: {}\nYear: {}\nMileage: {}\n".format(self.__make, self.__model, self.__year, self.__mileage)
       

       
        
def sortByMileage(car):
    return car.mileage

def sortByModel(car):
    return car.model
    
def sortByMake(car):
    return car.make
    
def sortByYear(car):
    return car.year
        
        
        
        
def carsByYear(carsList):
    return sorted((sorted((sorted((sorted(carsList, key = sortByMileage)), key = sortByModel)), key = sortByMake)), key = sortByYear, reverse = True)
    
 
 
def filterCars(carsList, minYear, maxYear, minKM, maxKM):
    carsList = list(filter(lambda car: (minYear <= car.year <= maxYear) and (minKM <= car.mileage <= maxKM), carsList))
    return sorted((sorted((sorted((sorted(carsList, key = sortByMileage)), key = sortByYear)), key = sortByModel)), key = sortByMake)
        
        
