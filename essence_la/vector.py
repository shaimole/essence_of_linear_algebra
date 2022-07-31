class Vector:
    def __init__(self, elements):
        self.elements = elements

    def add(self, vector):
        add_elements = lambda a,b: a+b
        sum  = map(add_elements, self.elements, vector.elements)
        return Vector(list(sum))
        
