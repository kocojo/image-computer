from sympy import sympify, sqrt
from sympy.parsing.latex import parse_latex

def evaluate_latex_expression(latex_expr):
    try:
        # Chuyển chuỗi LaTeX thành biểu thức SymPy
        expr = parse_latex(latex_expr)
        # Tính toán giá trị của biểu thức
        result = expr.evalf()
        return result
    except Exception as e:
        return f"Error in parsing or evaluating the expression: {e}"

# Ví dụ sử dụng:
latex_input = r"72^{2}+19"
result = evaluate_latex_expression(latex_input)
print(f"Kết quả của biểu thức {latex_input} là: {result}")