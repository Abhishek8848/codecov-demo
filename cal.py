from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs addition with type safety."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b

def sub(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs subtraction with type safety."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a - b

def mult(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs multiplication and prevents overflow errors."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    
    result = a * b

    # Handle float overflow by returning 'inf'
    if abs(result) > 1e308:
        return float('inf')  # Standard Python behavior

    return result

def div(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Performs division while handling zero and small number underflows."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    result = a / b

    # Avoid underflow for very small numbers
    if abs(result) < 1e-308:
        return 0.0  

    return result

# Example usage
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", sub(10, 4))
    print("Multiplication:", mult(1e308, 2))  # Should return 'inf'
    print("Division:", div(10, 2))
