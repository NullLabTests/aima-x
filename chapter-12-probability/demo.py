#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 12: Quantifying Uncertainty
"""

print("=" * 70)
print("Quantifying Uncertainty")
print("=" * 70)

print()
print("Bayesian probability example.")
print()


p_rain = 0.3
p_clouds_given_rain = 0.8

posterior = p_rain * p_clouds_given_rain

print("Posterior probability:", posterior)


print()
print("✅ Demo completed")
