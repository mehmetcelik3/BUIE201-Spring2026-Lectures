import factorial

def test_1():
    assert factorial.factorial(0) == 1

def test_2():
    assert factorial.factorial(3) == 6

def test_3():
    assert factorial.factorial(-1) == None

