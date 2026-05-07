#!/usr/bin/env python3

import os

chapters = sorted([
    d for d in os.listdir(".")
    if d.startswith("chapter-")
])

print("=" * 70)
print("AIMA-X V2 :: Educational AI Systems")
print("=" * 70)

for i, chapter in enumerate(chapters, start=1):
    print(f"{i:02d}. {chapter}")

choice = input("\nSelect chapter: ")

try:
    idx = int(choice) - 1
    selected = chapters[idx]

    os.system(f'python "{selected}/demo.py"')

except Exception as e:
    print("Error:", e)
