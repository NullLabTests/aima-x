#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 21: Deep Learning
"""

print("=" * 70)
print("Deep Learning")
print("=" * 70)

print()
print("Simple neuron activation.")
print()


weights = [0.2, 0.5]
inputs = [1.0, 2.0]

activation = sum(
    w * i for w, i in zip(weights, inputs)
)

print("Neuron activation:", activation)


print()
print("✅ Demo completed")
