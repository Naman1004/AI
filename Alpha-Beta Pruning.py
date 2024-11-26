# Alpha-Beta Pruning implementation
import math

# A simple utility function to evaluate leaf nodes
def evaluate(state):
    return state

# Minimax with Alpha-Beta Pruning
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # If we reach a leaf node, return its value
    if depth == 0 or node_index >= len(values):
        return evaluate(values[node_index])
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Assume binary tree (0 and 1 for left and right child)
            value = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, value)
            alpha = max(alpha, value)
            
            # Pruning
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Assume binary tree (0 and 1 for left and right child)
            value = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, value)
            beta = min(beta, value)
            
            # Pruning
            if beta <= alpha:
                break
        return min_eval

# Example usage:
if __name__ == "__main__":
    # Leaf node values of a binary tree
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = 3  # Tree depth
    alpha = -math.inf
    beta = math.inf

    result = alpha_beta_pruning(depth, 0, True, values, alpha, beta)
    print("Optimal value:", result)
