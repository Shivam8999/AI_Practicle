from queue import PriorityQueue

# Graph and heuristic values as per the provided image
graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 99,'F':9,'A':2},
    'C': {'B': 1},
    'D': {'E': 6, 'F': 1},
    'E': {'A': 3,'D':6},
    'F': {'B': 9, 'D': 1},
}

# Heuristic values for the nodes (h-values)
heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'F': 0
}

# A* algorithm implementation
def a_star_algorithm(graph, heuristic, start, goal):
    # Priority queue to hold nodes with their costs (f = g + h)
    open_list = PriorityQueue()
    open_list.put((0, start))  # (f-cost, node)
    
    # To track visited nodes
    closed_list = set()
    
    # To track the actual costs from start to each node (g-costs)
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    
    # To track the path
    parents = {start: None}
    
    while not open_list.empty():
        # Get the node with the lowest f-cost
        _, current = open_list.get()
        
        # If goal is reached, reconstruct the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1], g_costs[goal]  # Return path and cost
        
        closed_list.add(current)
        
        # Explore neighbors
        for neighbor, weight in graph[current].items():
            if neighbor in closed_list:
                continue
            
            # Calculate tentative g-cost
            tentative_g_cost = g_costs[current] + weight
            
            # If this path to neighbor is better, update details
            if tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                open_list.put((f_cost, neighbor))
                parents[neighbor] = current
    
    # If no path is found
    return None, float('inf')

# Main function to execute the algorithm
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'E'
    path, cost = a_star_algorithm(graph, heuristic, start_node, goal_node)
    
    if path:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")
