#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 13: Probabilistic Reasoning
"""

print("=" * 70)
print("Probabilistic Reasoning")
print("=" * 70)

print()
print("Simple Bayesian network dependency.")
print()


network = {
    "Rain": ["WetGrass"]
}

for parent, child in network.items():
    print(parent, "causes", child[0])


print()
print("✅ Demo completed")
