from essence_la.vector import Vector
from essence_la.vector import format_for_quiver
import pytest
import numpy as np

def test_import_vector_class():
    vec = Vector([1, 1])

def test_import_np_vector_class():
    vec = np.array([1, 1])

def test_add_vectors():
    vec1 = Vector([1, 3])
    vec2 = Vector([2, -1])
    sum = vec1.add(vec2)
    assert sum == Vector([3, 2])

def test_np_add_vectors():
    vec1 = np.array([1, 3])
    vec2 = np.array([2, -1])
    sum = np.add(vec1, vec2)
    assert sum.all() == np.array([3, 2]).all()

def test_scale_vectors():
    vec = Vector([2.0, 1.1, 0.5])
    product = vec.scale(3)
    assert product == Vector([6.0, 3.3, 1.5]) 

def test_np_scale_vectors():
    vec = np.array([2.0, 1.1, 0.5])
    product = np.multiply(vec, 3)
    assert product.all() == np.array([6.0, 3.3, 1.5]).all()

def test_format_for_quiver():
    with pytest.raises(Exception) as e:
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([-1, 3])
        format_for_quiver([vec1,vec2])
    assert 'Vectors do not have the same Dimensions' in str(e)
        
    vec1 = Vector([1, 2])
    vec2 = Vector([-1, 3])
    positions = format_for_quiver([vec1,vec2])
    assert positions == [[0, 0], [0, 0], [1, -1], [2, 3]]

def test_format_for_quiver_with_orgin():
    vec1 = Vector([1, 2]).set_origin([0, 0])
    vec2 = Vector([3, -1]).set_origin(vec1.elements)
    positions = format_for_quiver([vec1,vec2])
    assert positions == [[0, 1], [0, 2], [1, -1], [2, 3]]

