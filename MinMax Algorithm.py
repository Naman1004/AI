def minimax(depth, node_index, is_maximizing_player, scores, height):
    """
    A simple implementation of the Min-Max algorithm.

    Args:
        depth (int): Current depth in the tree.
        node_index (int): Index of the current node in the tree.
        is_maximizing_player (bool): True if it's the maximizer's turn, False otherwise.
        scores (list): List of terminal node values (scores).
        height (int): Height of the game tree.

    Returns:
        int: The optimal value for the current player.
    """
    # Base case: Leaf node is reached
    if depth == height:
        return scores[node_index]

    if is_maximizing_player:
        # Maximizer's turn: Choose the maximum value
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        # Minimizer's turn: Choose the minimum value
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# Example usage:
if __name__ == "__main__":
    # Terminal values of the leaf nodes
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    height = 3  # Height of the tree (log2 of number of scores)

    print("Optimal value:", minimax(0, 0, True, scores, height))
