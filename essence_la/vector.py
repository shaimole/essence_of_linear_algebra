class Vector:
    def __init__(self,elements):
        self.elements = elements

    def add(self,vector):
        sum  = map( lambda a,b: a+b,self.elements, vector.elements)
        return self.__class__(list(sum))
        
