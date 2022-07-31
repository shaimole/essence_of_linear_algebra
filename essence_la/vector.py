from numpy import void


class Vector:
    def __init__(self, elements: list[float]):
        self.elements = elements

    def __str__(self) -> str:
        return self.elements

    def __eq__(self, other) -> bool:
        return self.elements == other.elements

    def add(self, vector) -> 'Vector':
        add_elements = lambda a,b: a+b
        sum  = map(add_elements, self.elements, vector.elements)
        return Vector(list(sum))
        
