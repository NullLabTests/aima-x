#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 09: Inference Systems
"""

print("=" * 70)
print("Inference Systems")
print("=" * 70)

print()
print("Forward chaining demonstration.")
print()


facts = {"rain"}
rules = {
    "rain": "wet"
}

derived = set()

for fact in facts:

    if fact in rules:
        derived.add(rules[fact])

print("Derived facts:", derived)


print()
print("✅ Demo completed")
