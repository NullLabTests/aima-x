import random

agents = {
    "alpha": 0,
    "beta": 0,
    "gamma": 0
}

for tick in range(20):

    actor = random.choice(list(agents.keys()))

    delta = random.randint(-2, 5)

    agents[actor] += delta

    print(
        f"Tick={tick:02d} "
        f"Agent={actor} "
        f"Delta={delta}"
    )

print("\nFinal agent scores:\n")

for a in agents:
    print(a, agents[a])
