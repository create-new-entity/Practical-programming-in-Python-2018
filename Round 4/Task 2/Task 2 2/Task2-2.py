class Point2D:
    __slots__ = ("__x", "__y")
    
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
        
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
        
    def __str__(self):
        return "Point2D(x={:.1f}, y={:.1f})".format(self.__x, self.__y)
        
        
class Rectangle:
    __slots__ = ("__ll", "__ur")
    
    def __init__(self, p1 = Point2D(), p2 = Point2D()):
        if (p1.x < p2.x):
            llX = p1.x
            urX = p2.x
        else:
            llX = p2.x
            urX = p1.x
        if (p1.y < p2.y):
            llY = p1.y
            urY = p2.y
        else:
            llY = p2.y
            urY = p1.y
        
        self.ll = Point2D(llX, llY)
        self.ur = Point2D(urX, urY)
        
    @property
    def ll(self):
        return self.__ll
    @ll.setter
    def ll(self, ll):
        self.__ll = ll
        
    @property
    def ur(self):
        return self.__ur
    @ur.setter
    def ur(self, ur):
        self.__ur = ur
        
    def __str__(self):
        return "Rectangle(ll={}, ur={})".format(str(self.ll), str(self.ur))
        
         