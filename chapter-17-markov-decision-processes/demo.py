#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 17: Markov Decision Processes
"""

print("=" * 70)
print("Markov Decision Processes")
print("=" * 70)

print()
print("Simple value iteration step.")
print()


states = {
    "A": 1,
    "B": 3
}

updated = {
    s: v * 0.9
    for s, v in states.items()
}

print(updated)


print()
print("✅ Demo completed")
