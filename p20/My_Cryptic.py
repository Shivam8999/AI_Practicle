from itertools import permutations

# Function to check if the current digit mapping satisfies the equation
def is_valid(mapping):
    # Extract the mapped digits
    c = mapping['C']
    r = mapping['R']
    o = mapping['O']
    s = mapping['S']
    a = mapping['A']
    d = mapping['D']
    n = mapping['N']
    g = mapping['G']
    e = mapping['E']
    
    # Calculate the numerical values based on the mapping
    cross = c * 10000 + r * 1000 + o * 100 + s * 10 + s  # CROSS = C, R, O, S, S
    roads = r * 10000 + o * 1000 + a * 100 + d * 10 + s  # ROADS = R, O, A, D, S
    danger = d * 100000 + a * 10000 + n * 1000 + g * 100 + e * 10 + r  # DANGER = D, A, N, G, E, R
    
    # Check if the equation holds true: CROSS + ROADS = DANGER
    return cross + roads == danger

# Function to solve the cryptarithmetic equation CROSS + ROADS = DANGER
def solve_cryptarithmetic():
    # Letters involved in the equation: C, R, O, S, A, D, N, G, E
    letters = 'CROSSADNGER'
    digits = range(10)  # Digits from 0 to 9

    # Generate permutations of digits and map them to the letters
    for perm in permutations(digits, len(set(letters))):  # Fixed syntax error here
        # Create a dictionary to map the letters to digits
        mapping = dict(zip(set(letters), perm))
        
        # Check leading digits constraint (C, R, and D can't be zero)
        if mapping['C'] == 0 or mapping['R'] == 0 or mapping['D'] == 0:
            continue
        
        # Check if the current mapping satisfies the equation
        if is_valid(mapping):
            print(f"Solution found: {mapping}")
            return  # Stop after the first valid solution

# Main function to execute the program
if __name__ == "__main__":
    solve_cryptarithmetic()
