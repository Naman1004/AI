from itertools import permutations

def solve_crypto_arithmetic():
    # Assign unique digits to each letter
    letters = 'SENDMORY'  # Unique letters in the puzzle
    for perm in permutations(range(10), len(letters)):
        # Map each letter to a digit
        mapping = dict(zip(letters, perm))
        
        # Ensure no leading zeros in SEND, MORE, or MONEY
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Calculate SEND, MORE, and MONEY
        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']

        # Check if SEND + MORE == MONEY
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            return mapping  # Return the first valid mapping
    
    print("No solution found.")
    return None

# Run the solver
solve_crypto_arithmetic()
