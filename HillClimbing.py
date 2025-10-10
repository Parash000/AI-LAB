import random

N = 4

def print_board(state):
    for row in range(N):
        line = ""
        for col in range(N):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print("\n")

# Heuristic function: number of pairs of queens attacking each other
def heuristic(state):
    h = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                h += 1
    return h

# Hill climbing algorithm
def hill_climbing():
    # Random initial state
    current = [random.randint(0, N-1) for _ in range(N)]
    steps = 0

    while True:
        print(f"Step {steps}: {current} (Heuristic={heuristic(current)})")
        print_board(current)
        if heuristic(current) == 0:
            print("Solution found!")
            return current
        
        neighbors = []
        for col in range(N):
            for row in range(N):
                if row != current[col]:
                    neighbor = list(current)
                    neighbor[col] = row
                    neighbors.append(neighbor)
        
        # Choose the neighbor with the lowest heuristic
        current = min(neighbors, key=heuristic)
        steps += 1
        
        # If no improvement, restart
        if heuristic(current) >= heuristic(neighbors[0]):
            print("Stuck in local maxima, restarting...\n")
            current = [random.randint(0, N-1) for _ in range(N)]
            steps = 0

# Run the algorithm
solution = hill_climbing()
