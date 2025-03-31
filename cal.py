def add(a: int, b: int) -> int:
    return a + b

# Example usage
result = add(5, 3)

def sub(a: int, b: int) -> int:
    return a - b

def mult(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
