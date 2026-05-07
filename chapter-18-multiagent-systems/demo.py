#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 18: Multiagent Systems
"""

print("=" * 70)
print("Multiagent Systems")
print("=" * 70)

print()
print("Two agents competing for reward.")
print()


agents = {
    "agent_a": 10,
    "agent_b": 12
}

winner = max(agents, key=agents.get)

print("Winner:", winner)


print()
print("✅ Demo completed")
