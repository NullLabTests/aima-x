#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 10: Knowledge Representation
"""

print("=" * 70)
print("Knowledge Representation")
print("=" * 70)

print()
print("Semantic network graph example.")
print()


knowledge = {
    "bird": ["animal"],
    "sparrow": ["bird"]
}

for entity, parent in knowledge.items():
    print(entity, "->", parent)


print()
print("✅ Demo completed")
