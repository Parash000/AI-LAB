graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

goal = 'E'

# Depth-Limited Search (DLS) with step printing
def DLS(node, goal, depth, path=[]):
    path = path + [node]
    print(f"Visiting Node: {node}, Depth Limit: {depth}, Path: {path}")
    
    if node == goal:
        return True
    if depth <= 0:
        return False
    
    for child in graph.get(node, []):
        if DLS(child, goal, depth - 1, path):
            return True
    return False

# Iterative Deepening DFS
def IDDFS(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n--- Searching with Depth Limit: {depth} ---")
        found = DLS(start, goal, depth)
        if found:
            print(f"\nGoal '{goal}' found at depth {depth}!")
            return True
    print(f"\nGoal '{goal}' not found within depth {max_depth}")
    return False

# Run IDDFS
IDDFS('A', goal, 5)
