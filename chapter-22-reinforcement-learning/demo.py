#!/usr/bin/env python3

"""
AIMA-X Chapter 22
Reinforcement Learning
"""

print("=" * 70)
print("AIMA-X :: Chapter 22")
print("Reinforcement Learning")
print("=" * 70)

print()
print("Q-learning and RL.")
print()


import random

q_table = {}

states = ["A", "B", "C"]
actions = ["left", "right"]

for state in states:
    q_table[state] = {a: 0.0 for a in actions}

for episode in range(10):

    state = random.choice(states)

    action = random.choice(actions)

    reward = random.randint(0, 10)

    q_table[state][action] += 0.1 * reward

print("Q-table:")
print(q_table)


print()
print("✅ Demo completed")
