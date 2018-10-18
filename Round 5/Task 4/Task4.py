

class Point2D:
    __slots__ = ("__x", "__y")
    
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
    
    def __str__(self):
        return "Point2D(x={:.1f}, y={:.1f})".format(self.__x, self.__y)
        
    def __lt__(self, other):
        return (self.__x, self.__y) < (other.__x, other.__y)
        
    def __eq__(self, other):
        return (self.__x == other.__x) and (self.__y == other.__y)
        
        
class Triangle:
    __slots__ = ("__corners",)
    
    def __init__(self, p1 = Point2D(0,0), p2 = Point2D(1,0), p3 = Point2D(0,1)):
        self.__corners = [p1, p2, p3]
        self.__corners.sort()
        
    @property
    def p1(self):
        return self.__corners[0]
        
    @p1.setter
    def p1(self, p1):
        self.__corners[0] = p1
        self.__corners.sort()
        
    @property
    def p2(self):
        return self.__corners[1]
        
    @p2.setter
    def p2(self, p2):
        self.__corners[1] = p2
        self.__corners.sort()
        
    @property
    def p3(self):
        return self.__corners[2]
        
    @p3.setter
    def p3(self, p3):
        self.__corners[2] = p3
        self.__corners.sort()
        
        
    def __str__(self):
        return "Triangle(p1=" + str(self.p1) + ", p2=" + str(self.p2) + ", p3=" + str(self.p3) + ")"
        
    def __eq__(self, other):
        return (self.p1 == other.p1) and (self.p2 == other.p2) and (self.p3 == other.p3)
        
    