"""
Scientific computing tool
"""

import ast
import math
import operator

from langchain.tools import tool


class SafeEvaluator(ast.NodeVisitor):

    # Supported binary operations
    BIN_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
    }

    # Supported unary operations
    UNARY_OPS = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    # Supported functions
    SAFE_FUNCS = {
        "sqrt": math.sqrt,
        "exp": math.exp,
        "log": math.log,
        "log2": math.log2,
        "log10": math.log10,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "abs": abs,
    }

    def visit(self, node):
        return super().visit(node)

    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_Name(self, node):
        # Explicitly prohibit variable names
        raise ValueError(f"Variables not supported: {node.id}")

    def visit_BinOp(self, node):
        # Check binary operators
        op_type = type(node.op)
        if op_type not in self.BIN_OPS:
            raise ValueError(f"Unsupported binary operator: {op_type}")
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.BIN_OPS[op_type](left, right)

    def visit_UnaryOp(self, node):
        # Check unary operators
        op_type = type(node.op)
        if op_type not in self.UNARY_OPS:
            raise ValueError(f"Unsupported unary operator: {op_type}")
        operand = self.visit(node.operand)
        return self.UNARY_OPS[op_type](operand)

    def visit_Call(self, node):
        # Check function calls
        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function call format")

        func_name = node.func.id
        if func_name not in self.SAFE_FUNCS:
            raise ValueError(f"Unsupported function: {func_name}")

        if len(node.args) != 1:
            raise ValueError(f"{func_name} function requires exactly one argument")

        arg = self.visit(node.args[0])
        return self.SAFE_FUNCS[func_name](arg)

    def visit_Constant(self, node):
        if not isinstance(node.value, (int, float)):
            raise ValueError(f"Only integers or floats are supported, not {type(node.value).__name__}")
        return node.value

    def generic_visit(self, node):
        # Reject all nodes not in the whitelist
        raise ValueError(f"Unsupported syntax: {type(node).__name__}")

    def evaluate(self, expression: str) -> float | int:
        # Safely evaluate mathematical expressions
        if not expression.strip():
            raise ValueError("Expression cannot be empty")

        try:
            tree = ast.parse(expression, mode="eval")
            result = self.visit(tree)

            if isinstance(result, (int, float)):
                return result
            else:
                raise ValueError(f"Invalid result type: {type(result)}")
        except ZeroDivisionError:
            raise ValueError("Division by zero error")
        except ValueError as e:
            raise
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {str(e)}")


@tool()
def calculator(expression: str) -> str:
    """
    Safely evaluate mathematical expressions

    Supported operators: + - * / ** ()
    Supported functions: sqrt exp log log2 log10 sin cos tan abs

    Note: The above functions only support single arguments. Expressions like log(9, 3) are not supported.
    Example: Calculate (sqrt(9) + 1) ** 2
    """
    evaluator = SafeEvaluator()
    result = evaluator.evaluate(expression)
    return str(result)
