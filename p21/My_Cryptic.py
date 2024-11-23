from itertools import permutations

# Function to check if the current digit mapping satisfies the equation
def is_valid(mapping):
    # Extract the mapped digits
    g = mapping['G']
    o = mapping['O']
    t = mapping['T']
    u = mapping['U']
    
    # Calculate the numerical values based on the mapping
    go = g * 10 + o  # Two-digit number formed by G and O
    to = t * 10 + o  # Two-digit number formed by T and O
    out = o * 100 + u * 10 + t  # Three-digit number formed by O, U, and T
    
    # Check if the equation holds true: GO + TO = OUT
    return go + to == out

# Function to solve the cryptarithmetic equation GO + TO = OUT
def solve_cryptarithmetic():
    # Letters involved in the equation: G, O, T, U, N
    letters = 'GOTU'
    digits = range(10)  # Digits from 0 to 9

    # Generate permutations of digits and map them to the letters
    for perm in permutations(digits, len(letters)):

        # Create a dictionary to map the letters to digits
        mapping = dict(zip(letters, perm))
        
        # Check leading digits constraint (G and T can't be zero)
        if mapping['G'] == 0 or mapping['T'] == 0:
            continue
        
        # Check if the current mapping satisfies the equation
        if is_valid(mapping):
            print(f"Solution found: {mapping}")
            return  # Stop after the first valid solution

# Main function to execute the program
if __name__ == "__main__":
    solve_cryptarithmetic()
