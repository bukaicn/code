def add(a,b):
    return a + b

def pyreduce(a,b):
    return a - b

def test_add():
    assert add(2,6) == 8

def test_pyreduce():
    assert pyreduce(8,3)==5