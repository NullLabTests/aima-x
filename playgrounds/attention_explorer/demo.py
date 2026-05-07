tokens = [
    "Transformers",
    "changed",
    "AI"
]

attention = [
    [0.7, 0.2, 0.1],
    [0.3, 0.5, 0.2],
    [0.2, 0.2, 0.6]
]

print("\nAttention Matrix:\n")

for token, row in zip(tokens, attention):

    print(token, "->", row)
