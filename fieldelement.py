'''In this class we are trying to have finite elment i.e an order number which is greater than zero
and less than largest . The largest nummber in sequence of 19 should be 18 i.e F19 ={1,2,3,..18} '''

class FieldElement():
    def __init__(self,num,prime):
        if num >= prime or num <0:
            error='num {} is not a field range 0 to {}'.format(num,prime -1)

            raise ValueError(error)
        self.num=num
        self.prime=prime
    def __repr__(self):
        return'fieldelement__ {}({})'.format(self.prime,self.num)

    def __eq__(self,other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    

    def __ne__(self,other):
        return not (self == other)

    def __add__(self,other):
        if self.prime != other.prime:
            raise TypeError('cannot add two element in the same fields')
        num= (self.num + other.num) % self.prime
        return self.__class__(num,self.prime)
    
    def __sub__(self,other):
        if self.prime != other.prime:
            raise TypeError('cannot add two element in the same fields')
        num= (self.num - other.num) % self.prime
        return self.__class__(num,self.prime)

    def __multi__(self,other):
        if self.prime != other.prime:
            raise TypeError('cannot add two element in the same fields')
        num= (self.num * other.num) % self.prime
        return self.__class__(num,self.prime)

    def __pow__(self,expontent):
        n=expontent % (self.prime - 1)
        num= pow(self.num,n,self.prime)
        return self.__class__(num ,self.prime)
    
    def __truediv__(self,other):
        if self.prime == other.prime:
            num=pow(self.num,self.prime -2)*other.num
            result=num % self.prime 
            return self.__class__(result,self.prime)
        