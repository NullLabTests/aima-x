#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 16: Decision Theory
"""

print("=" * 70)
print("Decision Theory")
print("=" * 70)

print()
print("Expected utility calculation.")
print()


choices = {
    "safe": 5,
    "risky": 10
}

best = max(choices, key=choices.get)

print("Best decision:", best)


print()
print("✅ Demo completed")
