#!/usr/bin/env python3

"""
AIMA-X Chapter 05
Adversarial Search And Games
"""

print("=" * 70)
print("AIMA-X :: Chapter 05")
print("Adversarial Search And Games")
print("=" * 70)

print()
print("Minimax and adversarial reasoning.")
print()


def minimax(depth, maximizing):

    if depth == 0:
        return 1

    if maximizing:
        return max(minimax(depth - 1, False),
                   minimax(depth - 1, False))
    else:
        return min(minimax(depth - 1, True),
                   minimax(depth - 1, True))

print("Minimax result:", minimax(4, True))


print()
print("✅ Demo completed")
