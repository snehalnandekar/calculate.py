from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(10, 20) == 30

def test_subtraction():
    assert subtract(20, 5) == 15

def test_multiplication():
    assert multiply(4, 5) == 20

def test_division():
    assert divide(20, 4) == 5

def test_negative_numbers():
    assert add(-5, 10) == 5

def test_division_by_zero():
    assert divide(10, 0) == "Cannot divide by zero"
