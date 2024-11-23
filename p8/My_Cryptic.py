from itertools import permutations

def is_valid(mapping):
    # Extract the mapped digits
    t = mapping['T']
    w = mapping['W']
    o = mapping['O']
    f = mapping['F']
    u = mapping['U']
    r = mapping['R']
    
    # Calculate the numerical values
    two = t * 100 + w * 10 + o
    four = f * 1000 + o * 100 + u * 10 + r
    
    # Check if the equation holds true
    return two + two == four

def solve_cryptarithmetic():
    letters = 'TWOFUR'
    digits = range(10)

    # Generate permutations of digits and map them to the letters
    for perm in permutations(digits, len(letters)):

        mapping = dict(zip(letters, perm))
        
        # Check leading digits constraint (T and F can't be zero)
        if mapping['T'] == 0 or mapping['F'] == 0:
            continue
        
        # Check if the current mapping is valid
        if is_valid(mapping):
            print(f"Solution found: {mapping}")
            return  # Stop after the first valid solution

if __name__ == "__main__":
    solve_cryptarithmetic()
