"""
Math calculation tool
"""

from langchain.tools import tool


@tool()
def add(a: float, b: float) -> float:
    """Add two numbers (supports integers and floats)"""
    return float(a) + float(b)


@tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers (supports integers and floats)"""
    return float(a) - float(b)


@tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers (supports integers and floats)"""
    return float(a) * float(b)


@tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers (supports integers and floats)"""
    if float(b) == 0:
        return "Error: Division by zero"
    return float(a) / float(b)
