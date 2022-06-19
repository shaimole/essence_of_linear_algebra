from essence_la.vector import Vector

def test_import_vector_class():
    vec = Vector([1,1])

def test_add_vectors():
    vec1 = Vector([1,3])
    vec2 = Vector([2,-1])
    assert vec1.add(vec2) == Vector([3,2])
