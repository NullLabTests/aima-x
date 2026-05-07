#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 22: Reinforcement Learning
"""

print("=" * 70)
print("Reinforcement Learning")
print("=" * 70)

print()
print("Simple Q-learning table update.")
print()


q = {
    "state": {
        "left": 0.0
    }
}

reward = 5

q["state"]["left"] += 0.1 * reward

print(q)


print()
print("✅ Demo completed")
