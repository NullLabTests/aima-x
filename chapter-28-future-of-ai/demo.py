#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 28: The Future of AI
"""

print("=" * 70)
print("The Future of AI")
print("=" * 70)

print()
print("Simple exponential capability growth simulation.")
print()


capability = 1.0

for year in range(5):

    capability *= 1.5

    print(f"Year {year}: {capability:.2f}")


print()
print("✅ Demo completed")
