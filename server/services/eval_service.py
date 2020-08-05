def safe_eval(expr_str):
    if expr_str:
        return eval(expr_str, {"__builtins__": None}, None)
    return "string is empty"