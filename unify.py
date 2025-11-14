def unify(x, y, substitutions=None):
    if substitutions is None:
        substitutions = {}

    # Apply current substitutions
    x = substitute(x, substitutions)
    y = substitute(y, substitutions)

    # If both are the same variable or constant
    if x == y:
        return substitutions

    # If x is a variable
    if is_variable(x):
        return unify_variable(x, y, substitutions)

    # If y is a variable
    if is_variable(y):
        return unify_variable(y, x, substitutions)

    # If both are compound expressions (functions/predicates)
    if is_compound(x) and is_compound(y):
        if x[0] != y[0] or len(x[1]) != len(y[1]):
            return None  # function symbols or arities differ
        for xi, yi in zip(x[1], y[1]):
            substitutions = unify(xi, yi, substitutions)
            if substitutions is None:
                return None
        return substitutions

    # Otherwise, they can’t be unified
    return None


def unify_variable(var, x, substitutions):
    if var in substitutions:
        return unify(substitutions[var], x, substitutions)
    elif occurs_check(var, x, substitutions):
        return None  # Avoid infinite loops like x = f(x)
    else:
        substitutions[var] = x
        return substitutions


def occurs_check(var, x, substitutions):
    """Prevent a variable from being unified with an expression containing itself."""
    if var == x:
        return True
    elif is_variable(x) and x in substitutions:
        return occurs_check(var, substitutions[x], substitutions)
    elif is_compound(x):
        return any(occurs_check(var, arg, substitutions) for arg in x[1])
    return False


def substitute(expr, substitutions):
    """Recursively apply substitutions to an expression."""
    if is_variable(expr) and expr in substitutions:
        return substitute(substitutions[expr], substitutions)
    elif is_compound(expr):
        return (expr[0], [substitute(arg, substitutions) for arg in expr[1]])
    else:
        return expr


def is_variable(x):
    return isinstance(x, str) and x[0].islower()


def is_compound(x):
    return isinstance(x, tuple) and isinstance(x[1], list)


# Example usage:
if __name__ == "__main__":
    # Expressions are represented as tuples: ("functor", [arg1, arg2, ...])
    expr1 = ("Q", ["a", ("g", ["x", "a"]), ("f", ["y"])])
    expr2 = ("Q", ["a", ("g", [("f", ["b"]), "a"]), "x"])

    result = unify(expr1, expr2)
    if result:
        print("Unification successful!")
        print("Substitutions:")
        for var, val in result.items():
            print(f"  {var} → {val}")
    else:
        print("Unification failed.")
