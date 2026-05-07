tokens = [
    "Transformers",
    "changed",
    "AI"
]

attention = [
    [0.7, 0.2, 0.1],
    [0.2, 0.6, 0.2],
    [0.1, 0.3, 0.6]
]

print("\nATTENTION MATRIX\n")

for token, row in zip(tokens, attention):
    print(token, "->", row)
