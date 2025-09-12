import heapq
import copy

# Goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                count += 1
    return count


def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def is_goal(state):
    return state == GOAL_STATE


def valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3


def heuristic_fn(state, heuristic):
    if heuristic == "manhattan":
        return manhattan_distance(state)
    elif heuristic == "misplaced":
        return misplaced_tiles(state)
    else:
        raise ValueError("Unknown heuristic: choose 'manhattan' or 'misplaced'")


def a_star(start_state, heuristic="manhattan"):
    visited = set()
    heap = []

    g = 0
    h = heuristic_fn(start_state, heuristic)
    f = g + h

    heapq.heappush(heap, (f, g, start_state, []))  # (f, g, state, path)

    while heap:
        f, g, state, path = heapq.heappop(heap)

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if is_goal(state):
            return path + [state]

        x, y = get_blank_pos(state)

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if valid(nx, ny):
                new_state = copy.deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_state_tuple = tuple(tuple(row) for row in new_state)
                if new_state_tuple not in visited:
                    new_g = g + 1
                    new_h = heuristic_fn(new_state, heuristic)
                    new_f = new_g + new_h
                    heapq.heappush(heap, (new_f, new_g, new_state, path + [state]))

    return None


def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print("")


# Example usage:
if __name__ == "__main__":
    # Change this to test different starting positions
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]

    print("Using Manhattan Distance Heuristic:")
    path_manhattan = a_star(start_state, heuristic="manhattan")
    if path_manhattan:
        print_path(path_manhattan)
        print(f"Total steps (Manhattan): {len(path_manhattan) - 1}")
    else:
        print("No solution found with Manhattan.")

    print("\nUsing Misplaced Tiles Heuristic:")
    path_misplaced = a_star(start_state, heuristic="misplaced")
    if path_misplaced:
        print_path(path_misplaced)
        print(f"Total steps (Misplaced Tiles): {len(path_misplaced) - 1}")
    else:
        print("No solution found with Misplaced Tiles.")
