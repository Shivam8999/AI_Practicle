from itertools import permutations

# Function to check if the current digit mapping satisfies the equation
def is_valid(mapping):
    # Extract the mapped digits
    s = mapping['S']
    e = mapping['E']
    n = mapping['N']
    d = mapping['D']
    m = mapping['M']
    o = mapping['O']
    r = mapping['R']
    y = mapping['Y']
    
    # Calculate the numerical values based on the mapping
    send = s * 1000 + e * 100 + n * 10 + d  # Four-digit number formed by S, E, N, D
    more = m * 1000 + o * 100 + r * 10 + e  # Four-digit number formed by M, O, R, E
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y  # Five-digit number formed by M, O, N, E, Y
    
    # Check if the equation holds true: SEND + MORE = MONEY
    return send + more == money

# Function to solve the cryptarithmetic equation SEND + MORE = MONEY
def solve_cryptarithmetic():
    # Letters involved in the equation: S, E, N, D, M, O, R, Y
    letters = 'SENDMORY'
    digits = range(10)  # Digits from 0 to 9

    # Generate permutations of digits and map them to the letters
    for perm in permutations(digits, len(letters)):

        # Create a dictionary to map the letters to digits
        mapping = dict(zip(letters, perm))
        
        # Check leading digits constraint (S and M can't be zero)
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        
        # Check if the current mapping satisfies the equation
        if is_valid(mapping):
            print(f"Solution found: {mapping}")
            return  # Stop after the first valid solution

# Main function to execute the program
if __name__ == "__main__":
    solve_cryptarithmetic()
