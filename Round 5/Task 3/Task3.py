class Car:
    __slots__ = ("__make", "__model", "__year", "__mileage")
    
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.__year = int(year)
        self.mileage = int(mileage)
        
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
        
    @property
    def year(self):
        return self.__year
        
    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = int(mileage)
        
    def __str__(self):
        return "Make: {}\nModel: {}\nYear: {}\nMileage: {}\n".format(self.__make, self.__model, self.__year, self.__mileage)
        
    def __lt__(self, other):
        return (self.__make, self.__model, self.__year, self.__mileage) < (other.__make, other.__model, other.__year, other.__mileage)
        
    def __eq__(self, other):
        if(self.__make == other.__make and self.__model == other.__model and self.__year == other.__year):
            return True
        return False
        
        

