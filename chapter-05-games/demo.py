#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 05: Adversarial Search
"""

print("=" * 70)
print("Adversarial Search")
print("=" * 70)

print()
print("Simple minimax recursion example.")
print()


def minimax(depth, maximizing):

    if depth == 0:
        return 1

    if maximizing:
        return max(
            minimax(depth - 1, False),
            minimax(depth - 1, False)
        )

    return min(
        minimax(depth - 1, True),
        minimax(depth - 1, True)
    )

print("Minimax value:", minimax(4, True))


print()
print("✅ Demo completed")
