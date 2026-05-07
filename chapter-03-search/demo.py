#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 03: Graph Search
"""

print("=" * 70)
print("Graph Search")
print("=" * 70)

print()
print("Breadth-first search over a graph.")
print()


from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

visited = set()
queue = deque(["A"])

while queue:

    node = queue.popleft()

    if node not in visited:

        print("Visited:", node)

        visited.add(node)

        queue.extend(graph[node])


print()
print("✅ Demo completed")
