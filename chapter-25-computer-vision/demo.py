#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 25: Computer Vision
"""

print("=" * 70)
print("Computer Vision")
print("=" * 70)

print()
print("Edge detection concept using arrays.")
print()


image = [
    [0, 0, 1],
    [1, 1, 0]
]

edges = []

for row in image:
    edges.append(max(row) - min(row))

print("Detected edges:", edges)


print()
print("✅ Demo completed")
