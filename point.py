''' this is a class of elliptic curve that searchs whether the cordinates follow y^2 =x^3 + ax +b
where bitcoin elliptic curve y^2 =x^3 + 7 which is called secp256k1 '''


class Point():
    def __init__(self,  x, y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return

        if self.y ** 2 != self.x ** 3 + (self.a * self.x) + self.b:
            raise ValueError('the ({},{}) coordinates are not in the curve '.format(self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self,other):
        return not (self == other) 
    
    def __add__(self,other):
        if self.x !=other.x and self.y != other.y:
            raise TypeError('the {}{} coordinates are not equal '.format(self,other))
        
        if self.x is None:
            return other
        
        if other.x is None:
            return self
    :
        if self.x == other.x and self.y != other.y:
            return __class__(None,None,self.a,self.b)
        
        if self.x != other.x:
            s=(self.y - other.y)/(self.x -other.x)
            _x =s**2 -self.x -other.x
            _y =s *(self.x - _x) -self.y

            return __class__(_x,_y,self.a,self.b)
        
        if self == other:
            s=(3 * self.x ** 2 + self.a)/(2 * self.y)
            _x =s**2 - 2*self.x
            _y =s *(self.x - _x) -self.y

            return __class__(_x,_y,self.a,self.b)


        if self == other and self.y == 0*self.x:
            return __class__(None,None,self.a,self.b)
