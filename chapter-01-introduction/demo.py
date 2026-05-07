#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 01: Introduction to AI
"""

print("=" * 70)
print("Introduction to AI")
print("=" * 70)

print()
print("Simple reflex agent interacting with an environment.")
print()


class ReflexAgent:

    def perceive(self, env):
        return env

    def act(self, percept):

        if percept == "dirty":
            return "clean"

        return "idle"

agent = ReflexAgent()

for state in ["dirty", "clean"]:
    action = agent.act(agent.perceive(state))
    print(f"Environment: {state} -> Action: {action}")


print()
print("✅ Demo completed")
