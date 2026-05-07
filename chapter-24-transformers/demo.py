#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 24: Transformers and Attention
"""

print("=" * 70)
print("Transformers and Attention")
print("=" * 70)

print()
print("Simple attention weight example.")
print()


tokens = ["AI", "changes", "everything"]

attention = [0.2, 0.6, 0.2]

for token, weight in zip(tokens, attention):
    print(token, "->", weight)


print()
print("✅ Demo completed")
