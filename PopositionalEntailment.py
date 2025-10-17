import itertools

def pl_true(expr, model):
    if isinstance(expr, str):
        return model[expr]
    op = expr[0]
    if op == 'not':
        return not pl_true(expr[1], model)
    elif op == 'and':
        return pl_true(expr[1], model) and pl_true(expr[2], model)
    elif op == 'v':  # or
        return pl_true(expr[1], model) or pl_true(expr[2], model)
    elif op == '=>':  # implies
        return (not pl_true(expr[1], model)) or pl_true(expr[2], model)
    elif op == '<=>':  # iff
        return pl_true(expr[1], model) == pl_true(expr[2], model)
    else:
        raise ValueError("Unknown operator: " + op)


def extract_symbols(*exprs):
    symbols = set()
    for expr in exprs:
        if isinstance(expr, str):
            symbols.add(expr)
        elif isinstance(expr, tuple):
            for e in expr[1:]:
                symbols.update(extract_symbols(e))
    return symbols


def pretty(expr):
    if isinstance(expr, str):
        return expr
    op = expr[0]
    if op == 'not':
        return f"¬{pretty(expr[1])}"
    elif op == 'and':
        return f"({pretty(expr[1])} ∧ {pretty(expr[2])})"
    elif op == 'v':
        return f"({pretty(expr[1])} ∨ {pretty(expr[2])})"
    elif op == '=>':
        return f"({pretty(expr[1])} → {pretty(expr[2])})"
    elif op == '<=>':
        return f"({pretty(expr[1])} ↔ {pretty(expr[2])})"
    else:
        return str(expr)


def tt_entails(kb, query):
    symbols = list(extract_symbols(kb, query))
    all_models = list(itertools.product([False, True], repeat=len(symbols)))

    print(f"\nTruth Table for: KB |= {pretty(query)}")
    print(f"{' | '.join(symbols)} | KB | Query | Considered?")
    print("-" * (4 * len(symbols) + 14))

    all_true = True
    for vals in all_models:
        model = dict(zip(symbols, vals))
        kb_val = pl_true(kb, model)
        query_val = pl_true(query, model)
        considered = "✓" if kb_val else "-"
        print(f"{' | '.join(['T' if v else 'F' for v in vals])} | "
              f"{'T' if kb_val else 'F'} | "
              f"{'T' if query_val else 'F'} | {considered}")

        if kb_val and not query_val:
            all_true = False

    return all_true


def print_kb_truth_table():
    # Sentences in KB
    sentence1 = ('=>', 'Q', 'P')              # Q → P
    sentence2 = ('=>', 'P', ('not', 'Q'))     # P → ¬Q
    sentence3 = ('v', 'Q', 'R')                # Q ∨ R


    kb = ('and', sentence1, ('and', sentence2, sentence3))

    symbols = sorted(list(extract_symbols(kb)))
    all_models = list(itertools.product([False, True], repeat=len(symbols)))

    print("Truth Table for KB sentences:")
    header = symbols + [pretty(sentence1), pretty(sentence2), pretty(sentence3), "KB True?"]
    print(" | ".join(header))
    print("-" * (7 * len(header)))

    for vals in all_models:
        model = dict(zip(symbols, vals))
        val1 = pl_true(sentence1, model)
        val2 = pl_true(sentence2, model)
        val3 = pl_true(sentence3, model)
        kb_val = val1 and val2 and val3

        row_vals = [ 'T' if model[s] else 'F' for s in symbols ]
        row_vals += ['T' if val1 else 'F', 'T' if val2 else 'F', 'T' if val3 else 'F', 'T' if kb_val else 'F']

        print(" | ".join(row_vals))

    print("\nModels where KB is True:")
    for vals in all_models:
        model = dict(zip(symbols, vals))
        val1 = pl_true(sentence1, model)
        val2 = pl_true(sentence2, model)
        val3 = pl_true(sentence3, model)
        kb_val = val1 and val2 and val3
        if kb_val:
            print({s: ('T' if model[s] else 'F') for s in symbols})

    return kb


def main():
    kb = print_kb_truth_table()


    queries = [
        'R',
        ('=>', 'R', 'P'),
        ('=>', 'Q', 'R')
    ]

    for query in queries:
        result = tt_entails(kb, query)
        print(f"\nDoes KB entail {pretty(query)}? {'✅ Yes' if result else '❌ No'}")

if __name__ == "__main__":
    main()
