#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 27: AI Ethics and Safety
"""

print("=" * 70)
print("AI Ethics and Safety")
print("=" * 70)

print()
print("Simple alignment scoring example.")
print()


actions = {
    "help_human": 10,
    "ignore_request": -5
}

best = max(actions, key=actions.get)

print("Aligned action:", best)


print()
print("✅ Demo completed")
