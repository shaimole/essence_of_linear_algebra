from essence_la.vector import Vector

def test_import_vector_class():
    vec = Vector([1, 1])

def test_add_vectors():
    vec1 = Vector([1, 3])
    vec2 = Vector([2, -1])
    sum = vec1.add(vec2)
    assert sum == Vector([3, 2])

def test_scale_vectors():
    vec = Vector([2.0, 1.1, 0.5])
    product = vec.scale(3)
    assert product == Vector([6.0, 3.3, 1.5]) 