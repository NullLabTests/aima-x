import random

states = ["A", "B", "C"]

q = {
    s: {"left": 0.0, "right": 0.0}
    for s in states
}

for episode in range(30):

    state = random.choice(states)

    action = random.choice(["left", "right"])

    reward = random.randint(-5, 10)

    q[state][action] += 0.1 * reward

    print(
        f"Episode={episode:02d} "
        f"State={state} "
        f"Action={action} "
        f"Reward={reward}"
    )

print("\nLearned Policy:\n")

for s in q:
    print(s, q[s])
