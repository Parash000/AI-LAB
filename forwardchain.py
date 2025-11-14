# Forward Chaining Algorithm Implementation

def forward_chaining(KB, facts, query):
    """
    KB: list of rules in form ['A ^ B => C']
    facts: list of known facts
    query: fact to be inferred
    """
    inferred = set(facts)   # already known facts
    rules = KB.copy()

    print("Initial Facts:", inferred)
    print("Query:", query)
    print("\n--- Forward Chaining Process ---")

    while True:
        applied = False

        for rule in rules:
            premise, conclusion = rule.split("=>")
            premise = premise.strip()
            conclusion = conclusion.strip()
            conditions = [p.strip() for p in premise.split("^")]

            # Check if all conditions are true
            if all(cond in inferred for cond in conditions) and conclusion not in inferred:
                print(f"Rule applied: {rule}")
                inferred.add(conclusion)
                applied = True

                if conclusion == query:
                    print("\n✅ Query", query, "successfully inferred!")
                    print("Final Facts:", inferred)
                    return True

        if not applied:
            break

    print("\n❌ Query", query, "cannot be inferred from the given facts.")
    print("Final Facts:", inferred)
    return False


# Example usage
if __name__ == "__main__":
    # Knowledge Base
    KB = [
        "A ^ B => C",
        "C ^ D => E",
        "E => F"
    ]

    # Known facts
    facts = ["A", "B", "D"]

    # Query to prove
    query = "F"

    forward_chaining(KB, facts, query)
