#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 20: Learning Probabilistic Models
"""

print("=" * 70)
print("Learning Probabilistic Models")
print("=" * 70)

print()
print("Maximum likelihood estimate.")
print()


observations = [1, 1, 0, 1, 1]

estimate = sum(observations) / len(observations)

print("MLE estimate:", estimate)


print()
print("✅ Demo completed")
