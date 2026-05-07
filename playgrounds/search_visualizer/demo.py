from collections import deque

maze = [
    ["S", ".", ".", "#", "."],
    [".", "#", ".", "#", "."],
    [".", "#", ".", ".", "."],
    [".", ".", "#", "#", "."],
    [".", ".", ".", "G", "."]
]

ROWS = len(maze)
COLS = len(maze[0])

start = (0, 0)

queue = deque([start])

visited = set()

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

print("\nBFS Maze Exploration:\n")

while queue:

    r, c = queue.popleft()

    if (r, c) in visited:
        continue

    visited.add((r, c))

    print(f"Visited: {(r, c)}")

    if maze[r][c] == "G":
        print("\nGoal reached!")
        break

    for dr, dc in directions:

        nr, nc = r + dr, c + dc

        if (
            0 <= nr < ROWS and
            0 <= nc < COLS and
            maze[nr][nc] != "#"
        ):
            queue.append((nr, nc))
