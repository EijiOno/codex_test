#!/usr/bin/env python3
"""Simple command line calculator."""
import ast
import operator
import sys

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def eval_expr(expr: str) -> float:
    """Safely evaluate an arithmetic expression."""
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](left, right)
            raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](operand)
            raise ValueError(f"Unsupported unary operator: {op_type}")
        else:
            raise TypeError(f"Unsupported expression: {node}")

    parsed = ast.parse(expr, mode="eval")
    return _eval(parsed.body)


def main() -> None:
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
    else:
        expr = input("Enter expression: ")
    try:
        result = eval_expr(expr)
        print(result)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
