# calculator_plus.py

def multiply(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        return "Error"

def divide(a, b):
    try:
        if float(b) == 0:
            return "Error (Division by zero)"
        return float(a) / float(b)
    except ValueError:
        return "Error"