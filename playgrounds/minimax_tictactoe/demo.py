def minimax(depth, maximizing):

    if depth == 0:
        return 1

    if maximizing:
        return max(
            minimax(depth - 1, False),
            minimax(depth - 1, False)
        )

    return min(
        minimax(depth - 1, True),
        minimax(depth - 1, True)
    )

print("\nMinimax Evaluation:\n")

score = minimax(5, True)

print("Predicted utility:", score)
