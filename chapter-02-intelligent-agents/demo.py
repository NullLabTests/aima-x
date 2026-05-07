#!/usr/bin/env python3

"""
AIMA-X V2
Chapter 02: Intelligent Agents
"""

print("=" * 70)
print("Intelligent Agents")
print("=" * 70)

print()
print("PEAS-style rational taxi agent example.")
print()


class TaxiAgent:

    def choose_action(self, traffic):

        if traffic == "heavy":
            return "reroute"

        return "continue"

agent = TaxiAgent()

for traffic in ["light", "heavy"]:
    print(f"Traffic: {traffic}")
    print("Action:", agent.choose_action(traffic))


print()
print("✅ Demo completed")
