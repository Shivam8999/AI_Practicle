from queue import PriorityQueue

# Room dimensions (10x10 grid)
ROOM_WIDTH = 10
ROOM_HEIGHT = 10

# Object dimensions (rectangles + squares)
OBJECTS = [(2, 4), (3, 2), (4, 2), (2, 3), (3, 4), (2, 2), (3, 3), (4, 4), (2, 2)]

# Heuristic function: Remaining space estimation
def heuristic(remaining_objects, remaining_space):
    # Total area of remaining objects
    total_object_area = sum(w * h for w, h in remaining_objects)
    return max(0, remaining_space - total_object_area)

# Check if an object can be placed at position (x, y)
def can_place(room, obj, x, y):
    obj_width, obj_height = obj
    if x + obj_width > ROOM_WIDTH or y + obj_height > ROOM_HEIGHT:
        return False  # Out of bounds
    for i in range(y, y + obj_height):
        for j in range(x, x + obj_width):
            if room[i * ROOM_WIDTH + j] == 1:  # Position already occupied
                return False
    return True

# Place an object in the room
def place_object(room, obj, x, y):
    obj_width, obj_height = obj
    new_room = room[:]  # Create a copy of the room
    for i in range(y, y + obj_height):
        for j in range(x, x + obj_width):
            new_room[i * ROOM_WIDTH + j] = 1
    return new_room

# A* algorithm for object arrangement
def arrange_objects_a_star():
    # Initialize the room (1D grid, 0 = empty, 1 = occupied)
    initial_room = [0] * (ROOM_WIDTH * ROOM_HEIGHT)
    total_room_area = ROOM_WIDTH * ROOM_HEIGHT
    
    # Priority queue for A* search
    open_list = PriorityQueue()
    initial_state = (0, initial_room, OBJECTS, total_room_area)  # (f-cost, room, remaining_objects, remaining_space)
    open_list.put(initial_state)
    
    visited = set()  # To track visited states
    
    while not open_list.empty():
        # Get the state with the lowest f-cost
        _, current_room, remaining_objects, remaining_space = open_list.get()
        
        # Goal check: All objects placed
        if not remaining_objects:
            return current_room, total_room_area - remaining_space  # Return final room state and used space
        
        # Hashable state for memoization
        room_state = tuple(current_room)
        if (room_state, tuple(remaining_objects)) in visited:
            continue
        visited.add((room_state, tuple(remaining_objects)))
        
        # Explore placements for the next object
        for i, obj in enumerate(remaining_objects):
            for y in range(ROOM_HEIGHT):
                for x in range(ROOM_WIDTH):
                    if can_place(current_room, obj, x, y):
                        # Place the object
                        new_room = place_object(current_room, obj, x, y)
                        new_remaining_objects = remaining_objects[:i] + remaining_objects[i + 1:]
                        new_remaining_space = remaining_space - (obj[0] * obj[1])
                        
                        # Early termination: Skip if not enough space
                        if new_remaining_space < 0:
                            continue
                        
                        # Calculate costs
                        g_cost = total_room_area - new_remaining_space  # Space used so far
                        h_cost = heuristic(new_remaining_objects, new_remaining_space)  # Estimated remaining space
                        f_cost = g_cost + h_cost
                        
                        # Add the new state to the priority queue
                        open_list.put((f_cost, new_room, new_remaining_objects, new_remaining_space))
    
    return None, 0  # If no solution found

# Display the room arrangement
def print_room(room):
    for i in range(ROOM_HEIGHT):
        row = room[i * ROOM_WIDTH:(i + 1) * ROOM_WIDTH]
        print(''.join(['#' if cell == 1 else '.' for cell in row]))

# Main function
if __name__ == "__main__":
    final_room, used_space = arrange_objects_a_star()
    if final_room:
        print("Arrangement of objects in the room:")
        print_room(final_room)
        print(f"Total used space: {used_space}")
        print(f"Unused space: {ROOM_WIDTH * ROOM_HEIGHT - used_space}")
    else:
        print("No valid arrangement found.")
