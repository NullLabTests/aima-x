#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 15: Probabilistic Programming
"""

print("=" * 70)
print("Probabilistic Programming")
print("=" * 70)

print()
print("Sampling random events.")
print()


import random

samples = [random.choice([0, 1]) for _ in range(10)]

print("Samples:", samples)


print()
print("✅ Demo completed")
