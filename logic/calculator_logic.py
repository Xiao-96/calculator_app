# calculator_logic.py

def add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error"

def subtract(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        return "Error"