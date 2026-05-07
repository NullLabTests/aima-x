#!/usr/bin/env python3

"""
AIMA-X Chapter 17
Making Complex Decisions
"""

print("=" * 70)
print("AIMA-X :: Chapter 17")
print("Making Complex Decisions")
print("=" * 70)

print()
print("Markov Decision Processes.")
print()


from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print("Visited:", node)
            visited.add(node)
            queue.extend(graph[node])

bfs("A")


print()
print("✅ Demo completed")
