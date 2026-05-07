#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 11: Automated Planning
"""

print("=" * 70)
print("Automated Planning")
print("=" * 70)

print()
print("Simple action sequence planner.")
print()


state = "hungry"

plan = []

if state == "hungry":
    plan.append("find_food")
    plan.append("eat")

print("Generated plan:")
print(plan)


print()
print("✅ Demo completed")
