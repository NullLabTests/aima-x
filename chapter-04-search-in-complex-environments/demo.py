#!/usr/bin/env python3

"""
AIMA-X Chapter 04
Search In Complex Environments
"""

print("=" * 70)
print("AIMA-X :: Chapter 04")
print("Search In Complex Environments")
print("=" * 70)

print()
print("Optimization and heuristic search.")
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

def astar(start, goal):

    pq = [(0, start)]
    visited = set()

    while pq:

        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Reached goal:", goal)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            priority = cost + weight + heuristic[neighbor]
            heapq.heappush(pq, (priority, neighbor))

astar("A", "D")


print()
print("✅ Demo completed")
