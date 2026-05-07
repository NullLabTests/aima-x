#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 06: Constraint Satisfaction Problems
"""

print("=" * 70)
print("Constraint Satisfaction Problems")
print("=" * 70)

print()
print("Simple map coloring constraint checker.")
print()


regions = {
    "A": "red",
    "B": "blue",
    "C": "red"
}

constraints = [
    ("A", "B"),
    ("B", "C")
]

valid = True

for a, b in constraints:

    if regions[a] == regions[b]:
        valid = False

print("Constraint satisfaction:", valid)


print()
print("✅ Demo completed")
