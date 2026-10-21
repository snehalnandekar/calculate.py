# Simple Python Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test the calculator manually
print("Addition:", add(10, 20))
print("Subtraction:", subtract(20, 5))
print("Multiplication:", multiply(4, 5))
print("Division:", divide(20, 4))
