#!/usr/bin/env python3

import os

print("=" * 60)
print("AIMA-X :: AI Engineering Launcher")
print("=" * 60)

chapters = sorted([
    d for d in os.listdir(".")
    if d.startswith("chapter-")
])

for i, chapter in enumerate(chapters, start=1):
    print(f"{i:02d}. {chapter}")

print()
choice = input("Select chapter number: ")

try:
    idx = int(choice) - 1
    selected = chapters[idx]

    path = os.path.join(selected, "demo.py")

    print(f"\nLaunching {selected}...\n")

    os.system(f'python "{path}"')

except Exception as e:
    print("Invalid selection:", e)
