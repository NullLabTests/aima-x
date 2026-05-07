#!/usr/bin/env python3

import os

print("=" * 70)
print("AIMA-X V3 :: AI Engineering Lab")
print("=" * 70)

targets = sorted([
    d for d in os.listdir(".")
    if d.startswith("chapter-") or d == "playgrounds"
])

for i, target in enumerate(targets, start=1):
    print(f"{i:02d}. {target}")

choice = input("\nSelect target: ")

try:

    idx = int(choice) - 1
    selected = targets[idx]

    if selected == "playgrounds":
        print("\nAvailable playgrounds:\n")

        for file in os.listdir("playgrounds"):
            print(" -", file)

    else:
        os.system(f'python "{selected}/demo.py"')

except Exception as e:
    print("Error:", e)
