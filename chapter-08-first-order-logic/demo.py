#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 08: First Order Logic
"""

print("=" * 70)
print("First Order Logic")
print("=" * 70)

print()
print("Representing facts about humans.")
print()


facts = {
    "Socrates": "human"
}

for entity, kind in facts.items():

    if kind == "human":
        print(entity, "is mortal")


print()
print("✅ Demo completed")
