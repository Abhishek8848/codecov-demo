from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs addition with robust type handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b

def sub(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs subtraction with robust type handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a - b

def mult(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs multiplication with robust type handling and overflow detection."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    
    result = a * b

    # Overflow check for large floating point numbers
    if abs(result) > 1e308:
        raise OverflowError("Multiplication result is too large")
    
    return result

def div(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs division with zero handling, type safety, and floating-point precision."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    result = a / b

    # Handling small float precision errors
    if abs(result) < 1e-308:
        return 0.0  # Avoid underflow
    
    return result

# Example usage
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", sub(10, 4))
    print("Multiplication:", mult(6, 7))
    print("Division:", div(10, 2))
