from numpy import void


class Vector:
    def __init__(self, elements: list[float]):
        self.elements = elements

    def __str__(self) -> str:
        return self.elements.__str__()

    def __eq__(self, other) -> bool:
        return self.elements == other.elements

    def add(self, vector: 'Vector') -> 'Vector':
        add_elements = lambda a,b: a+b
        sum  = map(add_elements, self.elements, vector.elements)
        return Vector(list(sum))

    def scale(self, scalar: float) -> 'Vector':
        scale_elements = lambda a: round(a*scalar, 15)
        product = map(scale_elements, self.elements)
        return Vector(list(product))

        
