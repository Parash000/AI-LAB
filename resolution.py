# Resolution Algorithm Implementation for Propositional Logic

def resolution(KB, query):
    """
    KB: list of clauses (each clause is a list of literals)
    query: the statement we want to prove (string)
    """

    # Negate the query and add to KB
    negated_query = negate(query)
    print(f"Negated Query: {negated_query}")
    KB = KB + [ [negated_query] ]

    print("\n--- Resolution Process ---")
    new = set()

    while True:
        n = len(KB)
        pairs = [(KB[i], KB[j]) for i in range(n) for j in range(i + 1, n)]

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if [] in resolvents:  # empty clause means contradiction
                print("\n✅ Query", query, "is proven TRUE by Resolution!")
                return True
            for res in resolvents:
                new.add(tuple(sorted(res)))

        # Stop if no new clauses can be added
        new_clauses = [list(c) for c in new if list(c) not in KB]
        if not new_clauses:
            print("\n❌ Query", query, "cannot be proven from the KB.")
            return False

        for clause in new_clauses:
            KB.append(clause)
            print("New clause added:", clause)


def resolve(ci, cj):
    """
    Perform resolution between two clauses.
    ci, cj: lists of literals
    Returns a list of resolvents.
    """
    resolvents = []
    for di in ci:
        for dj in cj:
            if di == negate(dj):
                new_clause = list(set(ci + cj))
                new_clause.remove(di)
                new_clause.remove(dj)
                resolvents.append(new_clause)
    return resolvents


def negate(literal):
    """Negate a literal (simple '~' prefix notation)."""
    if literal.startswith("~"):
        return literal[1:]
    else:
        return "~" + literal


# Example usage
if __name__ == "__main__":
    # Knowledge Base (in CNF)
    KB = [
        ["A", "B"],        # A ∨ B
        ["~B", "C"],       # ¬B ∨ C
        ["~C"],            # ¬C
    ]

    query = "A"  # We want to prove if A is true

    resolution(KB, query)
