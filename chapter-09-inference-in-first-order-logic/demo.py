#!/usr/bin/env python3

"""
AIMA-X Chapter 09
Inference In First Order Logic
"""

print("=" * 70)
print("AIMA-X :: Chapter 09")
print("Inference In First Order Logic")
print("=" * 70)

print()
print("Automated theorem proving.")
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
