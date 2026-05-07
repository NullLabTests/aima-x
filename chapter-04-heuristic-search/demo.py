#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 04: A* Search
"""

print("=" * 70)
print("A* Search")
print("=" * 70)

print()
print("Heuristic pathfinding example.")
print()


import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2)],
    "C": [("D", 1)],
    "D": []
}

heuristic = {
    "A": 4,
    "B": 2,
    "C": 1,
    "D": 0
}

pq = [(0, "A")]

while pq:

    cost, node = heapq.heappop(pq)

    print("Expanded:", node)

    if node == "D":
        break

    for neighbor, weight in graph[node]:
        heapq.heappush(
            pq,
            (cost + weight + heuristic[neighbor], neighbor)
        )


print()
print("✅ Demo completed")
