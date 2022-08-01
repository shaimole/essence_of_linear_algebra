class Vector:
    def __init__(self, elements: list[float]):
        self.elements = elements

    def __str__(self) -> str:
        return self.elements.__str__()

    def __eq__(self, other: 'Vector') -> bool:
        return self.elements == other.elements

    def add(self, vector: 'Vector') -> 'Vector':
        add_elements = lambda a,b: a+b
        sum  = map(add_elements, self.elements, vector.elements)
        return Vector(list(sum))

    def scale(self, scalar: float) -> 'Vector':
        scale_elements = lambda a: round(a*scalar, 15)
        product = map(scale_elements, self.elements)
        return Vector(list(product))

def format_for_quiver(vectors: list[Vector]) -> list[list]:
    if not is_same_dimension(vectors):
         raise ValueError('Vectors do not have the same Dimensions')
    it = iter(vectors)
    dimension = len(next(it).elements)
    x_pos = [0] * dimension
    y_pos = [0] * dimension
    vector_elements = map(lambda vector: vector.elements, vectors)
    directions_by_dimension = zip(*vector_elements)
    directions = list(map(list,directions_by_dimension))
    return [x_pos, y_pos, *directions]

def is_same_dimension(vectors: list[Vector]) -> bool:
    vector_length = lambda vector: len(vector.elements)
    return len(set(map(vector_length, vectors))) == 1

        
