#!/usr/bin/env python3

import os

print("=" * 70)
print("AIMA-X :: AI SYSTEMS LAB")
print("=" * 70)

targets = []

for folder in sorted(os.listdir(".")):

    if folder.startswith("playgrounds"):
        targets.append(folder)

    elif folder.startswith("chapter-"):
        targets.append(folder)

for i, t in enumerate(targets, start=1):
    print(f"{i:02d}. {t}")

choice = input("\nSelect target: ")

try:

    idx = int(choice) - 1

    target = targets[idx]

    if target == "playgrounds":

        print("\nPlaygrounds:\n")

        for item in os.listdir("playgrounds"):
            print("-", item)

    else:

        os.system(f'python "{target}/demo.py"')

except Exception as e:
    print("Error:", e)
